from datetime import date
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.maintenance import MaintenanceStore

@pytest.fixture
def maintenance(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'wardrobe.sqlite3'))
    garment=wardrobe.add('Winter Jacket','jacket','blue')
    return MaintenanceStore(wardrobe),garment['id']

def test_plan_and_schedule(maintenance):
    manager,gid=maintenance
    result=manager.plan(gid,'dry_clean',30)
    assert result['interval_days']==30
    due=manager.schedule('2026-10-23',0)
    assert len(due)==1 and due[0]['due_on']=='2026-10-23'

def test_history_and_future_schedule(maintenance):
    manager,gid=maintenance
    manager.plan(gid,'inspect',30)
    manager.record(gid,'inspect','2026-10-01','Checked buttons')
    assert manager.schedule('2026-10-23',7)==[]
    assert manager.schedule('2026-10-23',8)[0]['due_on']=='2026-10-31'
    assert manager.history(gid)[0]['notes']=='Checked buttons'

def test_old_event_does_not_replace_latest(maintenance):
    manager,gid=maintenance
    manager.plan(gid,'wash',10)
    manager.record(gid,'wash','2026-10-10')
    manager.record(gid,'wash','2026-10-01')
    assert manager.schedule('2026-10-23')[0]['due_on']=='2026-10-20'

def test_recommendations_and_existing_plan(maintenance):
    manager,gid=maintenance
    assert any(x['task']=='dry_clean' for x in manager.recommendations(gid))
    manager.plan(gid,'dry_clean',180)
    assert not any(x['task']=='dry_clean' for x in manager.recommendations(gid))

def test_invalid_inputs(maintenance):
    manager,gid=maintenance
    with pytest.raises(ValueError): manager.plan(gid,'wash',0)
    with pytest.raises(ValueError): manager.record(gid,'unknown','2026-10-01')
    with pytest.raises(ValueError): manager.record(gid,'wash','not-a-date')
    with pytest.raises(LookupError): manager.plan(9999,'wash',7)

def test_api_routes_registered():
    from vogue_engine.dashboards.router import app
    paths={route.path for route in app.routes}
    assert '/api/v1/wardrobe/maintenance/schedule' in paths
    assert '/api/v1/wardrobe/maintenance/garments/{garment_id}/plans' in paths

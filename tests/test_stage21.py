"""Stage 21 regression coverage for tailoring workflows."""
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.alterations import AlterationStore

@pytest.fixture
def service(tmp_path):
    wardrobe=WardrobeStore(str(tmp_path/'wardrobe.db'))
    garment=wardrobe.add('Jacket','outerwear','black')
    return AlterationStore(wardrobe),garment['id']

def test_job_lifecycle(service):
    s,g=service
    job=s.create(g,'Shorten sleeves',tailor='Local tailor',due_date='2026-12-15',estimated_cost=500)
    assert job['status']=='planned'
    assert s.transition(job['id'],'in_progress')['status']=='in_progress'
    assert s.transition(job['id'],'ready')['status']=='ready'
    assert s.transition(job['id'],'completed')['status']=='completed'
    assert [r['to_status'] for r in s.history(job['id'])]==['planned','in_progress','ready','completed']
    with pytest.raises(ValueError): s.transition(job['id'],'planned')

def test_costs_and_summary(service):
    s,g=service
    job=s.create(g,'Hem trousers',estimated_cost=250)
    s.update(job['id'],actual_cost=310,appointment_at='2026-11-01T10:30:00')
    summary=s.summary()
    assert summary['estimated_total']==250
    assert summary['actual_total']==310
    assert summary['total_jobs']==1

def test_invalid_data(service):
    s,g=service
    with pytest.raises(LookupError): s.create(999,'Fix zipper')
    with pytest.raises(ValueError): s.create(g,'Fix zipper',estimated_cost=-1)
    with pytest.raises(ValueError): s.create(g,'  ')
    with pytest.raises(ValueError): s.create(g,'Fix zipper',due_date='invalid')
    with pytest.raises(ValueError): s.create(g,'Fix zipper',appointment_at='invalid')

def test_filter_delete_and_cascade(service):
    s,g=service
    first=s.create(g,'Hem',due_date='2026-11-01')
    second=s.create(g,'Buttons',due_date='2026-12-01')
    assert len(s.list(due_before='2026-11-15'))==1
    s.transition(second['id'],'cancelled')
    assert len(s.list(status='cancelled'))==1
    assert s.delete(first['id'])
    assert not s.delete(first['id'])
    assert len(s.list())==1
    assert s.history(second['id'])[-1]['to_status']=='cancelled'

def test_routes_exist():
    from vogue_engine.dashboards.router import app
    paths={route.path for route in app.routes}
    assert '/api/v1/wardrobe/alterations/jobs' in paths
    assert '/api/v1/wardrobe/alterations/summary' in paths

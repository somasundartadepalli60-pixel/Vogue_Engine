"""Stage 10 lifecycle regression tests (no network or API credentials)."""
from datetime import date
import pytest
from vogue_engine.wardrobe.storage import WardrobeStore
from vogue_engine.wardrobe.sustainability import SustainabilityStore

@pytest.fixture
def setup(tmp_path):
    wardrobe = WardrobeStore(str(tmp_path / 'wardrobe.db'))
    garment = wardrobe.add('Blue jacket', 'outerwear', 'blue')
    return wardrobe, SustainabilityStore(wardrobe), garment['id']

def test_record_and_history(setup):
    _, ledger, gid = setup
    event = ledger.record(gid, 'donated', date(2026, 10, 23), 'Charity', 'Clean')
    assert event['action'] == 'donated'
    assert ledger.history(gid)[0]['recipient'] == 'Charity'

def test_reject_invalid_action(setup):
    _, ledger, gid = setup
    with pytest.raises(ValueError):
        ledger.record(gid, 'unknown', date.today())

def test_reject_missing_garment(setup):
    _, ledger, _ = setup
    with pytest.raises(LookupError):
        ledger.record(9999, 'recycled', date.today())

def test_report_and_year_filter(setup):
    _, ledger, gid = setup
    ledger.record(gid, 'repaired', date(2025, 1, 1))
    ledger.record(gid, 'recycled', date(2026, 1, 1))
    assert ledger.report()['total_events'] == 2
    assert ledger.report(2025)['reuse_event_percentage'] == 100.0
    assert ledger.report(2026)['reuse_event_percentage'] == 0.0

def test_delete_event(setup):
    _, ledger, gid = setup
    event = ledger.record(gid, 'resold', date.today())
    assert ledger.delete(event['id']) is True
    assert ledger.delete(event['id']) is False

def test_garment_deletion_cascades(setup):
    wardrobe, ledger, gid = setup
    ledger.record(gid, 'donated', date.today())
    wardrobe.delete(gid)
    assert ledger.history() == []

def test_no_unverified_environmental_metrics(setup):
    _, ledger, _ = setup
    report = ledger.report()
    assert report['total_events'] == 0
    assert report['reuse_event_percentage'] == 0
    assert 'methodology' in report

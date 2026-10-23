from datetime import date
from vogue_engine.wardrobe.tailoring_insights import build_insights


def test_empty_insights():
    assert build_insights([], date(2026, 10, 23)) == {'monthly': [], 'appointments': [], 'reminders': []}


def test_insights_appointments_expenses_and_overdue():
    jobs = [{'id': 1, 'status': 'planned', 'created_at': '2026-10-01 00:00:00',
             'estimated_cost': 100.25, 'actual_cost': 40.0, 'appointment_at': '2026-10-24T09:30:00',
             'due_date': '2026-10-22', 'description': 'Hem trousers', 'tailor': 'Local shop'},
            {'id': 2, 'status': 'completed', 'created_at': '2026-10-05 00:00:00',
             'estimated_cost': 30, 'actual_cost': None, 'appointment_at': '2026-10-25T11:00:00',
             'due_date': '2026-10-21', 'description': 'Fix seam', 'tailor': ''}]
    result = build_insights(jobs, date(2026, 10, 23))
    assert result['monthly'] == [{'month': '2026-10', 'estimated': 130.25, 'actual': 40.0, 'jobs': 2}]
    assert len(result['appointments']) == 1
    assert result['reminders'][0]['overdue'] is True
    assert len(result['reminders']) == 1

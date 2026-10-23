"""Pure, offline aggregation for tailoring calendars and spending reports."""
from collections import defaultdict
from datetime import date


def build_insights(jobs, today=None):
    today = today or date.today()
    today_iso = today.isoformat()
    monthly = defaultdict(lambda: {'estimated': 0.0, 'actual': 0.0, 'jobs': 0})
    appointments = []
    reminders = []
    for job in jobs:
        month = (job.get('created_at') or '')[:7]
        if len(month) == 7:
            entry = monthly[month]
            entry['jobs'] += 1
            entry['estimated'] += job.get('estimated_cost') or 0
            entry['actual'] += job.get('actual_cost') or 0
        appointment = job.get('appointment_at')
        if appointment and job['status'] not in ('completed', 'cancelled'):
            appointments.append({'id': job['id'], 'date': appointment[:10], 'time': appointment[11:16], 'tailor': job['tailor'], 'description': job['description']})
        due = job.get('due_date')
        if due and job['status'] not in ('completed', 'cancelled'):
            reminders.append({'id': job['id'], 'due_date': due, 'overdue': due < today_iso, 'description': job['description'], 'status': job['status']})
    for value in monthly.values():
        value['estimated'] = round(value['estimated'], 2)
        value['actual'] = round(value['actual'], 2)
    return {'monthly': [{'month': key, **monthly[key]} for key in sorted(monthly)],
            'appointments': sorted(appointments, key=lambda a: (a['date'], a['time'], a['id'])),
            'reminders': sorted(reminders, key=lambda r: (r['due_date'], r['id']))}

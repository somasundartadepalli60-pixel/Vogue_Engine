"""Offline lending analytics, calendar and dashboard reminders."""
from collections import Counter
from datetime import date, timedelta
from .lending import LendingStore, valid_date


def build_lending_insights(service: LendingStore, today=None, days=30):
    if not 1 <= days <= 366:
        raise ValueError('days must be between 1 and 366')
    current = date.fromisoformat(valid_date(today or date.today()))
    loans = service.list()
    active = [loan for loan in loans if loan['returned_at'] is None]
    overdue = [loan for loan in active if date.fromisoformat(loan['due_date']) < current]
    upcoming = [loan for loan in active if current <= date.fromisoformat(loan['due_date']) <= current + timedelta(days=days)]
    calendar = {}
    for loan in upcoming + overdue:
        key = loan['due_date']
        calendar.setdefault(key, []).append({'id': loan['id'], 'garment_id': loan['garment_id'], 'direction': loan['direction'], 'contact': loan['contact'], 'overdue': date.fromisoformat(key) < current})
    monthly = Counter(loan['start_date'][:7] for loan in loans)
    contacts = Counter(loan['contact'] for loan in loans)
    return {'today': current.isoformat(), 'window_days': days,
            'totals': {'all': len(loans), 'active': len(active), 'overdue': len(overdue), 'upcoming': len(upcoming), 'returned': len(loans)-len(active)},
            'calendar': [{'date': day, 'loans': calendar[day]} for day in sorted(calendar)],
            'overdue': sorted(overdue, key=lambda row: row['due_date']),
            'upcoming': sorted(upcoming, key=lambda row: row['due_date']),
            'monthly_activity': [{'month': month, 'loans': count} for month,count in sorted(monthly.items())],
            'frequent_contacts': [{'contact': name, 'loans': count} for name,count in contacts.most_common(10)]}

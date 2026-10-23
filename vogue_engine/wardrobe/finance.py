"""Offline wardrobe spending ledger and cost-per-wear analytics."""
from __future__ import annotations
import sqlite3
from datetime import date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from .storage import WardrobeStore

DDL = '''
CREATE TABLE IF NOT EXISTS garment_purchases (
 garment_id INTEGER PRIMARY KEY REFERENCES garments(id) ON DELETE CASCADE,
 price_minor INTEGER NOT NULL CHECK(price_minor>=0),
 currency TEXT NOT NULL DEFAULT 'INR',
 purchased_on TEXT NOT NULL,
 vendor TEXT NOT NULL DEFAULT '',
 notes TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS wardrobe_budgets (
 month TEXT PRIMARY KEY,
 amount_minor INTEGER NOT NULL CHECK(amount_minor>=0),
 currency TEXT NOT NULL DEFAULT 'INR'
);
CREATE INDEX IF NOT EXISTS idx_purchase_date ON garment_purchases(purchased_on);
'''

def minor_units(amount):
    try:
        value = Decimal(str(amount))
        if not value.is_finite() or value < 0 or value > Decimal('1000000000'):
            raise ValueError('Amount must be finite and between 0 and 1 billion')
        return int((value * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    except (InvalidOperation, TypeError) as exc:
        raise ValueError('Invalid monetary amount') from exc

def validate_currency(currency):
    if currency != 'INR':
        raise ValueError('Stage 7 supports INR only; currency conversion is not provided')
    return currency

def validate_date(value):
    try: return date.fromisoformat(value).isoformat()
    except (ValueError, TypeError) as exc: raise ValueError('Date must be YYYY-MM-DD') from exc

class FinanceStore:
    def __init__(self, wardrobe: WardrobeStore):
        self.wardrobe = wardrobe
        with self.wardrobe.connection() as db: db.executescript(DDL)

    def set_purchase(self, garment_id, amount, purchased_on, vendor='', notes='', currency='INR'):
        cents=minor_units(amount); purchased_on=validate_date(purchased_on);validate_currency(currency)
        if len(vendor)>120 or len(notes)>1000: raise ValueError('Vendor or notes too long')
        with self.wardrobe.connection() as db:
            if not db.execute('SELECT 1 FROM garments WHERE id=?',(garment_id,)).fetchone():
                raise LookupError('Garment not found')
            db.execute('''INSERT INTO garment_purchases(garment_id,price_minor,currency,purchased_on,vendor,notes)
                VALUES(?,?,?,?,?,?) ON CONFLICT(garment_id) DO UPDATE SET
                price_minor=excluded.price_minor,currency=excluded.currency,
                purchased_on=excluded.purchased_on,vendor=excluded.vendor,notes=excluded.notes''',
                (garment_id,cents,currency,purchased_on,vendor,notes))
        return self.get_purchase(garment_id)

    def get_purchase(self, garment_id):
        with self.wardrobe.connection() as db:
            row=db.execute('''SELECT p.*,g.name,g.category,g.wears FROM garment_purchases p
                JOIN garments g ON g.id=p.garment_id WHERE garment_id=?''',(garment_id,)).fetchone()
            return self._present(row) if row else None

    @staticmethod
    def _present(row):
        result=dict(row)
        result['amount']=result.pop('price_minor')/100
        result['cost_per_wear']=round(result['amount']/result['wears'],2) if result['wears'] else None
        return result

    def purchases(self, month=None):
        if month is not None: self._month(month)
        with self.wardrobe.connection() as db:
            rows=db.execute('''SELECT p.*,g.name,g.category,g.wears FROM garment_purchases p
                JOIN garments g ON g.id=p.garment_id WHERE (? IS NULL OR substr(p.purchased_on,1,7)=?)
                ORDER BY p.purchased_on DESC,p.garment_id''',(month,month)).fetchall()
            return [self._present(row) for row in rows]

    @staticmethod
    def _month(month):
        if len(month)!=7 or month[4]!='-': raise ValueError('Month must be YYYY-MM')
        validate_date(month+'-01')
        return month

    def set_budget(self, month, amount, currency='INR'):
        self._month(month);validate_currency(currency);cents=minor_units(amount)
        with self.wardrobe.connection() as db:
            db.execute('''INSERT INTO wardrobe_budgets(month,amount_minor,currency) VALUES(?,?,?)
                ON CONFLICT(month) DO UPDATE SET amount_minor=excluded.amount_minor,currency=excluded.currency''',
                (month,cents,currency))
        return self.monthly_summary(month)

    def monthly_summary(self, month):
        self._month(month)
        with self.wardrobe.connection() as db:
            spent=db.execute('SELECT COALESCE(SUM(price_minor),0) FROM garment_purchases WHERE substr(purchased_on,1,7)=?',(month,)).fetchone()[0]
            count=db.execute('SELECT COUNT(*) FROM garment_purchases WHERE substr(purchased_on,1,7)=?',(month,)).fetchone()[0]
            budget=db.execute('SELECT amount_minor FROM wardrobe_budgets WHERE month=?',(month,)).fetchone()
        limit=budget[0] if budget else None
        return {'month':month,'currency':'INR','spent':spent/100,'purchases':count,
                'budget':limit/100 if limit is not None else None,
                'remaining':(limit-spent)/100 if limit is not None else None,
                'over_budget':spent>limit if limit is not None else None}

    def overview(self):
        items=self.purchases()
        total=sum(minor_units(i['amount']) for i in items)
        return {'currency':'INR','total_spent':total/100,'tracked_garments':len(items),
                'never_worn':sum(i['wears']==0 for i in items),
                'most_expensive':sorted(items,key=lambda i:(-i['amount'],i['garment_id']))[:10],
                'best_value':sorted((i for i in items if i['wears']>0),key=lambda i:(i['cost_per_wear'],i['garment_id']))[:10]}

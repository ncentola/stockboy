from sqlalchemy.dialects.postgresql.json import JSONB
from datetime import datetime as dt
from app import db

class Transaction(db.Model):
    __tablename__       = 'transactions'
    id                  = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upc                 = db.Column(db.String(64))
    quantity            = db.Column(db.Integer)
    created_at          = db.Column(db.DateTime, default=dt.utcnow)

    def __init__(self, upc, quantity):
        self.upc        = upc
        self.quantity   = quantity

    def __repr__(self):
        return '<Transaction {}>'.format(self.id)

class Product(db.Model):
    __tablename__       = 'products'
    upc                 = db.Column(db.String(64), primary_key=True)
    data                = db.Column(JSONB)
    created_at          = db.Column(db.DateTime, default=dt.utcnow)

    def __init__(self, upc, data):
        self.upc        = upc
        self.data       = data

    def __repr__(self):
        return '<Product {}>'.format(self.id)

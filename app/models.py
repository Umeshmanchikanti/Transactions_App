# models.py
from app import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reason = db.Column(db.String(200), nullable=False)
    bill_image = db.Column(db.String(300), nullable=True)

    def __repr__(self):
        return f"<Transaction {self.id} - {self.reason}>"

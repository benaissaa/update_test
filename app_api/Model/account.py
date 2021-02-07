
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import relationship
from .db import db
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    malls = db.relationship('Mall', backref='account', lazy=True)  # Many to one 

    
    def __repr__(self):
        return '<Accountt %s>' % self.name
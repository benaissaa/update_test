from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import relationship
from .db import db
class Mall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    account_id=db.Column(db.Integer, db.ForeignKey('account.id'))
    
    unit = relationship("Unit", uselist=False, back_populates="mall") # one to one 
    

    def __repr__(self):
        return '<Mall %s>' % self.name        
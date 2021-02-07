from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import relationship
from .db import db




class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    mall_id=db.Column(db.Integer, db.ForeignKey('mall.id'))
    mall = relationship("Mall", back_populates="unit")  # one to one 

    def __repr__(self):
        return '<Unit %s>' % self.name
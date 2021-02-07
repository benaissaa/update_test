
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from Model import Account,Mall, Unit


ma = Marshmallow()
class AccountSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")
        model = Account


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)


class MallSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "account_id")
        model = Mall 

mall_schema = MallSchema()
malls_schema = MallSchema(many=True)  

class UnitSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "mall_id")
        model = Unit 

unit_schema = UnitSchema()
units_schema = UnitSchema(many=True)  
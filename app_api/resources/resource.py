from flask_restful import Resource, Api
from flask import Flask, request
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource,fields, marshal_with
from flask_restplus import Api, Resource ,fields
from flask import Blueprint
from Model import db, Account, Mall , Unit
from resources.shema import account_schema,accounts_schema,mall_schema,malls_schema,unit_schema,units_schema

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

mall_fields = {
    'name': fields.String,
    
    'account_id': fields.Integer
}


account_fields = {
    'name': fields.String,
    'malls': fields.List(fields.Nested(mall_fields))
}
unit_fields = {
    'name': fields.String,
    
    'mall_id': fields.Integer
}

account_definition = api.model('account Informations', {
   
    'name': fields.String(required=True)})

mall_definition = api.model('mall Informations', {
    'name': fields.String(required=True),
    'account_id': fields.Integer(required=True)
    })  

unit_definition = api.model('unit Informations', {
    'name': fields.String(required=True),
    'mall_id': fields.Integer(required=True)
    })    

class AccountListResource(Resource):
    def get(self):

        """
        returns a list of account with pagination
        """
        accounts = Account.query.all()
        return accounts_schema.dump(accounts)
        
    # @api.expect(account_definition)	
    def post(self):
            """
            Add a new account
            """
            new_account = Account(
            name=request.json['name'],
                
            )
            db.session.add(new_account)
            db.session.commit()
            
            return account_schema.dump(new_account)

       


class AccountResource(Resource):
    def get(self, account_id):
        """
        fetch an account with the given id + pagination
        """
        account = Account.query.get_or_404(account_id)
        return account_schema.dump(account)
        

    # @api.expect(account_definition)
    def patch(self, account_id):
        """
        update an account 
        """

        account = Account.query.get_or_404(account_id)
        
        if 'name' in request.json:
            account.name = request.json['name']
        
        db.session.commit()
        return account_schema.dump(account)
       
    def delete(self, account_id):
        """
        delete an account
        """

        account = Account.query.get_or_404(account_id)
        db.session.delete(account)
        db.session.commit()
        return '', 204



# __API Mall__




class MallListResource(Resource):

    def get(self):
        
        malls = Account.query.all()
        return malls_schema.dump(malls)

    #  @api.expect(mall_definition)
    def post(self):
        new_mall = Mall(
            name=request.json['name'],
            account_id=request.json['account_id'],
            
        )
        db.session.add(new_mall)
        db.session.commit()
        return mall_schema.dump(new_mall) 



class MallResource(Resource):

    def get(self, mall_id):
 
        mall = Mall.query.get_or_404(mall_id)
        return mall_schema.dump(mall)
    # @api.expect(mall_definition)
    def patch(self, mall_id):
        mall = Mall.query.get_or_404(mall_id)

        if 'name' in request.json:
            mall.name = request.json['name']
        if 'account_id' in request.json:
            mall.account_id  = request.json['account_id']


        db.session.commit()
        return mall_schema.dump(mall)

    def delete(self, mall_id):
        mall = Mall.query.get_or_404(mall_id)
        db.session.delete(mall)
        db.session.commit()
        return '', 204


class UnitListResource(Resource):

    def get(self):
        
        units = Account.query.all()
        return units_schema.dump(units)

    # @api.expect(unit_definition)
    def post(self):
        new_unit = Unit(
            name=request.json['name'],
            mall_id=request.json['mall_id'],
            
        )
        db.session.add(new_unit)
        db.session.commit()
        return unit_schema.dump(new_unit)


       

class UnitResource(Resource):

    def get(self, unit_id):
        unit = Unit.query.get_or_404(unit_id)
        return unit_schema.dump(unit)

    # @api.expect(unit_definition)
    def patch(self, unit_id):
        unit = Unit.query.get_or_404(unit_id)

        if 'name' in request.json:
            unit.name = request.json['name']
        if 'mall_id' in request.json:
            unit.mall_id  = request.json['mall_id']

        db.session.commit()
        return unit_schema.dump(unit)

    def delete(self, unit_id):
        unit = Unit.query.get_or_404(unit_id)
        db.session.delete(unit)
        db.session.commit()
        return '', 204    
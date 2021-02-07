from flask import Blueprint
from flask_restful import Api
from resources.resource import AccountListResource,AccountResource,MallListResource,MallResource,api_bp,api,UnitListResource,UnitResource
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource,fields, marshal_with
from flask_restplus import Api, Resource ,fields
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(AccountListResource, '/accounts')
api.add_resource(AccountResource, '/accounts/<int:account_id>')
api.add_resource( MallListResource, '/malls')
api.add_resource(MallResource, '/malls/<int:mall_id>')
api.add_resource( UnitListResource, '/units')
api.add_resource(UnitResource, '/units/<int:unit_id>')

from flask import Blueprint
from flask_restful import Api
from calculations.calculations_api.service_resource import AllContracts, \
    Contracts

bp = Blueprint('api_v1', __name__)
api_bp = Api(bp)

api_bp.add_resource(AllContracts, '/contracts')
api_bp.add_resource(Contracts, '/contracts/<string:product_name>')

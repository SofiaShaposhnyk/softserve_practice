from flask_restful import Resource
from calculations.db.helpers import get_contracts


class Contracts(Resource):
    def get(self, product_name):
        return get_contracts(product_name)


class AllContracts(Resource):
    def get(self):
        return get_contracts()

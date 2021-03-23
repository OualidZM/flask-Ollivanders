from flask_restful import Resource
from services import items

class GetItem(Resource):
    def get(self, item):
        getted_item = items.get_item(item)
        return getted_item
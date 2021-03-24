from flask import jsonify, Blueprint
from services import items

get_item = Blueprint("get_item", __name__)


@get_item.route("/item/<name>")
def get_item_func(name):
    response = items.get_item(name)
    return jsonify(response)

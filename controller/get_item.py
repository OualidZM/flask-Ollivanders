from flask import jsonify, Blueprint
from services import get_item

get_item = Blueprint("get_item", __name__)


@get_item.route("/item/<name>")
def get_item_func(name):
    response = get_item.get_item(name)
    return jsonify(response)

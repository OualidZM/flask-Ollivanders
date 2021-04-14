from flask import jsonify, Blueprint
from services import get_item

get_item_blue = Blueprint("get_item", __name__)


@get_item_blue.route("/item/<name>")
def get_item_func(name):
    response = get_item.get_item(name)
    return jsonify(response)

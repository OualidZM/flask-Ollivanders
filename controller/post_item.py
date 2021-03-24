from flask import redirect, Blueprint, request
from services import post_items

post_item_blue = Blueprint("post_item", __name__)


@post_item_blue.route("/item", methods=["POST"])
def post_item():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    post_items.post_item(name, int(sell_in), int(quality))
    return redirect("/")

from flask import Blueprint, request, redirect
from services import delete_item

delete_item_blue = Blueprint("delete_item", __name__)

@delete_item_blue.route("/item", methods=["DELETE"])
def delete_item_func():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    delete_item.delete_item(name, int(sell_in), int(quality))
    return redirect("/")

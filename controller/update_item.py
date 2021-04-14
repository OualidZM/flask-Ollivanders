from flask import redirect, Blueprint, request
from services.update_item import update_item as update_item_service

update_item_blue = Blueprint("update_item", __name__)


@update_item_blue.route("/item", methods=["PUT"])
def update_item():
    data = request.get_json()
    id = data["id"]
    new_name = data["new_name"]
    new_sell_in = data["new_sell_in"]
    new_quality = data["new_quality"]
    update_item_service(id, new_name, int(new_sell_in), int(new_quality))
    return redirect("/")

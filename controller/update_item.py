from flask import  Blueprint,request,redirect
from services import update

update_item_blue = Blueprint("update_item",__name__)

@update_item_blue.route("/",methods=["PUT"])

def update_itemm():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    update.update_item(name, int(sell_in), int(quality))
    return redirect("/")
from flask import  Blueprint,request,redirect
from services import update

update_item_blue = Blueprint("update_item",__name__)

@update_item_blue.route("/item",methods=["PUT"])

def update_itemm():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    new_sell_in = data["new_sell_in"]
    new_quality = data["new_quality"]
    # update.update_item(name,int(sell_in),int(new_sell_in))
    update.update_item(name, int(sell_in), int(quality),int(new_sell_in),int(new_quality))
    return redirect("/")
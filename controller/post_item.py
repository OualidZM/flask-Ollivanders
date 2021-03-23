from flask import redirect, jsonify, Blueprint
from services import post_items
post_item_blue = Blueprint('post_item', __name__)

@post_item_blue.route('/add/item/<name>/<sell_in>/<quality>', methods=['GET'])
def post_item(name, sell_in, quality):
    post_items.post_item(name, int(sell_in), int(quality))
    return redirect("/")

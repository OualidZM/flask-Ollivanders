from flask import Flask
from controller import get_item, post_item, get_all, delete_item,update_item


app = Flask(__name__)
app.register_blueprint(get_item.get_item)
app.register_blueprint(get_all.get_all_blue)
app.register_blueprint(post_item.post_item_blue)
app.register_blueprint(delete_item.delete_item_blue)
app.register_blueprint(update_item.update_item_blue)

if __name__ == "__main__":
    app.run(debug=True)

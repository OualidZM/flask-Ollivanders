from repository.sqlite_db import Database, Item


def update_item(id, new_name, new_sell_in, new_quality):
    db = Database("Ollivanders.sqlite")
    Item.db = db

    item_manager = Item.manager()
    item_to_update = item_manager.get(id=id)
    item_to_update.name = new_name
    item_to_update.sell_in = new_sell_in
    item_to_update.quality = new_quality
    item_to_update.update()
    db.commit()

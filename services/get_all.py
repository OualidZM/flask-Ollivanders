from repository import sqlite_db as DB


def get_all():
    manager = DB.item_manager()
    list_items = list(manager.all())
    data = {}
    for item in list_items:
        data[item.id] = {
            "name": item.name,
            "sell_in": item.sell_in,
            "quality": item.quality,
        }
    return data

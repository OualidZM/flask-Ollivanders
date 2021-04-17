from repository import sqlite_db as DB


def get_item(item):
    manager = DB.item_manager()
    try:
        item_db = manager.get(id=item)
        answer = {
            item_db.id: {
                "name": item_db.name,
                "quality": item_db.quality,
                "sell_in": item_db.sell_in,
            }
        }
    except ValueError:
        answer = {"none": "null"}
    return answer

from repository import sqlite_db as DB


# def get_item(item):
#     for item_list in BBDD.BBDD.inventory:
#         if item == item_list[0]:
#             answer = {
#                 "name": item_list[0],
#                 "sell_in": item_list[1],
#                 "quality": item_list[2],
#             }
#             break
#         else:
#             answer = {"none": "null"}
#     return answer
def get_item(item):
    manager = DB.item_manager()
    item_db = manager.get(id=item)
    answer = {item_db.id:{"name":item_db.name, "quality":item_db.quality, "sell_in":item_db.sell_in}}
    return answer

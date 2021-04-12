from repository.sqlite_db import item_manager, Database, Item
# from objects_temp.Updateable import update_quality
# from repository import BBDD

def update_item(name,sell_in,quality,new_sell_in,new_quality):
    db = Database('Ollivanders.sqlite')
    Item.db = db
    k = Item(name, sell_in, quality)
    zz = k.name
    if zz == name:
        sql = f"UPDATE Item SET sell_in = '{new_sell_in}', quality='{new_quality}' WHERE name ='{name}'"
        db.execute(sql)
        db.commit()
        db.close()

update_item("test_test", 55, 100, 9999999, 141413)
from repository.sqlite_db import item_manager, Database, Item

def update_item(name,sell_in,quality,new_sell_in,new_quality):
    db = Database('Ollivanders.sqlite')
    Item.db = db
    table = Item(name, sell_in, quality)
    names = table.name
    if names == name:
        sql = f"UPDATE Item SET sell_in = '{new_sell_in}', quality='{new_quality}' WHERE name ='{name}'"
        db.execute(sql)
        db.commit()
        db.close()

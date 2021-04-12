from repository.sqlite_db import item_manager, Database, Item

def post_item(name, sell_in, quality):
    db = Database('Ollivanders.sqlite')
    Item.db = db
    Item(name, sell_in, quality).save()
    db.commit()
    

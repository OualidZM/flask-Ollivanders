from repository.sqlite_db import Database


def delete_item(name, sell_in, quality):
    items = Database("Ollivanders.sqlite")
    sql = f"delete from Item where name='{name}' and sell_in='{sell_in}' and quality='{quality}'"
    items.execute(sql)
    items.commit()
    items.close()

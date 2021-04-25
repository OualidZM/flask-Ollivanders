from repository.sqlite_db import Database, Item
from repository.categories import categories


def update_daily(items):
    # conectamos la base de datos
    db = Database("Ollivanders.sqlite")
    Item.db = db
    # creamos el manager
    manager = Item.manager(db)
    # recorremos los datos de la base de datos
    for item in items.items():
        # por cada objeto, comprobamos cual es su categoria
        for category in categories.items():
            # si concuerda con alguna, es de esa, si no, es normalItem
            if category[0] in item[1]["name"]:
                checked = True
                new_item = category[1](
                    item[1]["name"], item[1]["quality"], item[1]["sell_in"]
                )
        if not checked:
            checked = False
            new_item = categories["Normal"](
                item[1]["name"], item[1]["quality"], item[1]["sell_in"]
            )
        # actualizmaos la quality y el sell_in
        new_item.update_quality()
        # cogemos el objeto de la base de datos con "x" id
        database_item = manager.get(item[0])
        # actualziamos sus parametros segun categoria de objeto
        database_item.quality = new_item.quality
        database_item.sell_in = new_item.sell_in
        # guardamos los cambios para el Modelo Item
        database_item.update()
        # Y al final guardamos los cambios para la base de datos
        db.commit()

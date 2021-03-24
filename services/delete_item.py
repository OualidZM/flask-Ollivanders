from repository import BBDD


def delete_item(name, sell_in, quality):
    BBDD.BBDD.inventory.remove([name, sell_in, quality])

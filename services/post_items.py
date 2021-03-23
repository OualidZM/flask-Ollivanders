from repository import BBDD

def post_item(name, sell_in, quality):
    BBDD.BBDD.inventory.append([name, sell_in, quality])
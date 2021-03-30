from repository import  BBDD


def update_item(name,sell_in,quality,new_name,new_sell_in,new_quality):
    BBDD.BBDD.inventory[name,sell_in,quality] = BBDD.BBDD.inventory[new_name,new_sell_in,new_quality]
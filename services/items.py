from repository import BBDD

def get_item(item):
    for item_list in BBDD.BBDD.inventory:
        if (item == item_list[0]):
            answer = item
            break
    return answer
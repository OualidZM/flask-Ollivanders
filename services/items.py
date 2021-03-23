from repository import BBDD

def get_item(item):
    for item_list in BBDD.BBDD.inventory:
        if (item == item_list[0]):
            answer = {
                "name":item_list[0],
                "sell_in":item_list[1],
                "quality":item_list[2]
            }
            break
        else:
            answer = {"none":"null"}
    return answer
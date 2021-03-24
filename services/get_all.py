from repository import BBDD


def get_all():
    answer = BBDD.BBDD.inventory
    data = []
    for array in answer:
        data.append({"name": array[0], "sell_in": array[1], "quality": array[2]})
    return data

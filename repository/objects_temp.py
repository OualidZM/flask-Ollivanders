from orm import Model

class Item(Model):
    name = str
    sell_in = int
    quality = int
    
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality



def __repr__(self):
    return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



class Updateable(Item):

    def update_quality(self):
        # update method
        pass


class NormalItem(Updateable):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def set_sell_in(self):
        self.sell_in -= 1

    def setQuality(self, valor):
        if self.quality + valor > 50:
            self.quality = 50
        elif self.quality + valor >= 0:
            self.quality = self.quality + valor
        else:
            self.quality = 0

    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.set_sell_in()


class ConjuredItem(NormalItem):

    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_quality(self):
        if self.sell_in >= 0:
            self.setQuality(-2)
        else:
            self.setQuality(-4)
        self.setSell_in()


class AgedBrie(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)


    def update_quality(self):
        if self.sell_in > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
        self.setSell_in()


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        self.quality = 80

class Backstage(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)


    def update_quality(self):
        if self.sell_in > 10:
            self.setQuality(1)
        elif self.sell_in > 5:
            self.setQuality(2)
        elif self.sell_in > 0:
            self.setQuality(3)
        else:
            self.quality = 0
        self.setSell_in()
class Cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives: list, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text=''):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        to_print = 'Type cake: {}'.format(self.__class__)
        super().show_info()
        to_print += '\nself.shape'
        to_print += '\nself.ornaments'
        to_print += '\nText: {}'.format(True if len(self.text) > 0 else False)
        print(to_print)
        # Future task, change output - move separator under new variables


cake01 = Cake('Big Cake', 'Cake', 'Vanilla', [], 'Strawberry jam')
sp_cake01 = SpecialCake('Crooked Cake', 'Special Cake', 'Chocolate', [], 'Prince Polo XXL',
                        'Birthday', 'Oval', 'Birthdays candles', 'Pablo')

cake01.show_info()
sp_cake01.show_info()
for x in SpecialCake.bakery_offer:
    print(x.full_name)

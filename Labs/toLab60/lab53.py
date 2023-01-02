from datetime import date
from datetime import timedelta


class Cake:
    """
    Class presenting a some cake which initialized
    """
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        Init method
        :param name: cake name
        :param kind: once of types cakes: [type1, type2, type3 ...]
        :param taste: carry taste
        :param additives: its optional argument which can be empy, to do it enter: []
        :param filling: chosen filling cake
        """
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
        """
        :return: returning name.upper() and kind of object (default type object is class Cake)
        """
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class Promo:

    def __init__(self, name, discount, start_date, end_date, minimal_order):

        self.name = name
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date
        self.minimal_order = minimal_order

    @property
    def full_name(self):
        return "PROMO {0:s} {1:.0%}".format(self.name, self.discount)


class PromoCake(Cake, Promo):

    def __init__(self, name: str, kind, taste, additives, filling, promo_name, discount, start_date, end_date, minimal_order):
        Cake.__init__(self, name, kind, taste, additives, filling)
        Promo.__init__(self, name.capitalize(), discount, start_date, end_date, minimal_order)


cake = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake.show_info()

promo10 = Promo("DISCOUNT - no additional conditions", 0.15, date.today(), date.today() + timedelta(days=14), 0)
print(promo10.full_name)

promo_cake_01 = PromoCake(cake.name, cake.kind, cake.taste, ['test', 'x'], cake.filling,
                          promo10.name, promo10.discount, promo10.start_date, promo10.end_date, promo10.minimal_order)
promo_cake_01.show_info()
print(promo_cake_01.full_name)
print(PromoCake.__mro__)

help(Cake.__init__)

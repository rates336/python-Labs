class Cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

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

    def add_additives(self, additives):
        self.additives.append(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')


class MemoryAdditives:
    list_of_current_additives = []

    def __init__(self, func):
        self.func = func

    def __call__(self, cake: Cake, additives: list):
        self.list_of_current_additives.extend(cake.additives)
        # self.list_of_current_additives = additives
        a = 0
        for x in additives:
            print(x)
            if x not in self.list_of_current_additives:
                self.list_of_current_additives.append(x)
                cake.add_additives(x)
            a += 1
            print(a)
        return self.list_of_current_additives


@MemoryAdditives
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


print(cake01.additives)
add_extra_additives(cake01, ['chocolate', 'nuts', 'strawberry'])
# add_extra_additives(cake01, 'strawberry')
print(cake01.additives)

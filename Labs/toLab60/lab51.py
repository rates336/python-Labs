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
        if type(additives) is str:
            self.additives.append(additives)
        elif type(additives) is list:
            self.additives.extend(additives)
        else:
            print('\n\n', '-' * 10, 'Error', '-' * 10, sep='')
            print(type(additives), 'has not implemented in {}'.format(type(self)))
            print('Please inject once of types:\tstr, list')
            print('-' * 10, 'Error', '-' * 10, '\n\n', sep='')

    def __iadd__(self, other):
        if isinstance(other, Cake):
            self.add_additives(other.additives)
        else:
            self.add_additives(other)
        return self

    def __str__(self):
        return '{}\nTaste: {}, Filling: {}, Additives: {}'.format(str(self.name + ':').upper(), str(self.taste).title(),
                                                                  str(self.filling).title(),
                                                                  True if len(self.additives) > 0 else False)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')
cake02 = Cake('Vanilla Cake', 'cake', 'vanilla', ['cream', 'jelly candy'], 'cream')
cake01.show_info()
cake01 += cake02
cake01 += 4
cake01.show_info()
print(cake01)



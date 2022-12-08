class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name: str, kind: str, taste: str, additives: list, filling: str, gluten_free: bool, text: str):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.__additives = additives.copy()
        self.__filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.cake_filling) > 0:
            print("Filling:     {}".format(self.cake_filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)

    @property
    def cake_filling(self):
        return self.__filling

    @cake_filling.setter
    def cake_filling(self, filling: str):
        self.__filling = filling

    @property
    def additives(self):
        return self.__additives

    @additives.setter
    def additives(self, additives: list):
        # for x in additives:
        #     self.__additives.append(x)
        self.__additives.extend(additives)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], '', False, '')
cake03 = Cake('Super Sweet Meringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

print(Cake.bakery_offer)
cake01.show_info()
print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake01.Text = 'Happy birthday!'
cake02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()

cake04.show_info()
cake04.additives(['kakao', 'apple jam'])
cake04.show_info()



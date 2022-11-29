cake_00 = {'taste': 'vanilla', 'glaze': 'chocolate', 'text': 'Happy Birthday', 'weight': 0.7}
cake_01 = {'taste': 'tee', 'glaze': 'lemon', 'text': 'Happy Python Coding', 'weight': 1.3}
cakes_list = [cake_00, cake_01]


def show_cake_info(cake: dict):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake.get('taste'), cake.get('glaze'), cake.get('text'), cake.get('weight')))


show_cake_info(cake_00)
show_cake_info(cakes_list[1])
print(list(map(lambda cake: '{} cake with {} glaze with text "{}" of {} kg'.format(
    cake.get('taste'), cake.get('glaze'), cake.get('text'), cake.get('weight')), cakes_list)))


def fill_bakery_offer():
    Cake.bakery_offer.append(Cake('Happy cake', 'sponge', 'chocolate', ['icing-sugar', 'm&m', 'kitkat'],
                                  'cherry', 'Happy Day :)', 'L'))
    Cake.bakery_offer.append(Cake('Fit cake', 'cheese_cake', 'carrot', ['banana', 'kiwi', 'nuts'],
                                  '', 'I am fit because I like it! :)', 'M'))
    Cake.bakery_offer.append(Cake('Chocko-power', 'chocolate_cake', 'chocolate',
                                  ['grated-chocolate', 'pieces of chocolate', 'white chocolate glaze'],
                                  'sparkling chocolate', 'I love cho co\nla te ;Q', 'XXL'))
    Cake.bakery_offer.append(Cake('Meringue', 'meringue', 'cream', [],
                                  'vanilla', 'beZZa :p', 'M'))


def show_bakery_offer():
    print(list(map(lambda cake: cake.info(), Cake.bakery_offer)))


class Cake:
    known_types = ['cake', 'muffin', 'pudding', 'meringue', 'cheese_cake', 'biscuit', 'waffle',
                   'eclair', 'christmas_cake', 'pretzel', 'sponge', 'jelly', 'other']
    bakery_offer = []
    __gluten_free = False
    __text = ''

    def __init__(self, name: str, kind: str, carry_taste: str, additions: list, filling: str,
                 text: str, size: str, __gluten_free=False):
        self.name = name
        if Cake.known_types.count(kind) > 0:
            self.kind = kind
        else:
            self.kind = 'other'
        self.carry_taste = carry_taste
        self.additions = additions
        self.filling = filling
        self.__text = text
        self.size = size
        Cake.bakery_offer.append(self)
        self.__gluten_free = __gluten_free

    def info(self):
        print(25 * '-')
        print(self.name)
        print('Kind: {}'.format(self.kind))
        print('Carry taste: {}'.format(self.carry_taste))
        print('Additions: {}\nFilling: {}'.format(self.additions, self.filling))
        print('Some text: {}, Size: {}'.format(len(self.text) > 0, self.size))
        print('Gluten free: {}'.format(self.__gluten_free))
        print(25 * '-')
        return self

    def set_filling(self, filling):
        self.filling = filling
        print('Completed set filling in cake: {}'.format(self))
        self.info()

    def add_additives(self, list_additions: list):
        for x in list_additions:
            self.additions.append(x)

    def get_text(self):
        return self.__text

    def set_text(self, new_text):
        if self.additions.count('frosting') > 0:
            self.__text = new_text
        else:
            print('Text can be only applied on type of glade: {}'.format('frosting'))


print('Today we offers:')
print(list(map(lambda cake: cake.name + ' and it\'s a ' + cake.kind, Cake.bakery_offer)))
# print(list(map(lambda cake: cake.name + '\nIt\'s a ' + (cake.kind + '\ '), bakery_offer)))
cake_03 = Cake('Happy cake', 'sponge_cake', 'chocolate', ['icing-sugar', 'm&m', 'kitkat'],
               'cherry', 'Happy Day :)', 'L')
cake_03.info()
# Cake.bakery_offer.append(cake_03)
Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'S', True)
# cake_02 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'S')
# Cake.__init__(cake_03, 'Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'L')
show_bakery_offer()
fill_bakery_offer()
print(40 * '*')
show_bakery_offer()
print(Cake.bakery_offer)
Cake.bakery_offer[-1].info()
Cake.bakery_offer[3].set_filling('2x vanilla')
Cake.bakery_offer[-1].add_additives(['whipped cream'])
Cake.bakery_offer[3].info()
Cake.bakery_offer[2].info()
Cake.bakery_offer.append(Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'S'))
Cake.bakery_offer[-1].info()

print(isinstance(cake_01, Cake))
print(isinstance(cake_03, Cake))
print(type(cake_03) is Cake)
print('vars Cake: {} \ndir Cake: {}'.format(vars(Cake), dir(Cake)))
print('vars cake_03: {} \ndir cake_03: {}'.format(vars(cake_03), dir(cake_03)))
print(vars(cake_03))
cake_03._Cake__gluten_free = True
print(vars(cake_03))
cake_03._Cake__gluten_free = False
print(vars(cake_03))
cake_03.__gluten_free = True
print(list(map(lambda cake: cake.name + '\nIt\'s a ' + (cake.kind + r'\\'), Cake.bakery_offer)))

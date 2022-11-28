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


def show_bakery_offer():
    print(Cake.bakery_offer)

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


class Cake:
    known_types = ['cake', 'muffin', 'pudding', 'meringue', 'cheese_cake', 'biscuit', 'waffle',
                   'eclair', 'christmas_cake', 'pretzel', 'sponge', 'jelly', 'other']
    bakery_offer = []

    def __init__(self, name: str, kind: str, carry_taste: str, additions: list, filling: str,
                 text: str, size: str):
        self.name = name
        if Cake.known_types.count(kind) > 0:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]
        self.carry_taste = carry_taste
        self.additions = additions
        self.filling = filling
        self.text = text
        self.size = size
        # fill_bakery_offer()
        Cake.bakery_offer.append(Cake('Happy cake', 'sponge', 'chocolate', ['icing-sugar', 'm&m', 'kitkat'],
                                  'cherry', 'Happy Day :)', 'L'))
        Cake.bakery_offer.append(Cake('Fit cake', 'cheese_cake', 'carrot', ['banana', 'kiwi', 'nuts'],
                                  '', 'I am fit because I like it! :)', 'M'))
        Cake.bakery_offer.append(Cake('Chocko-power', 'chocolate_cake', 'chocolate',
                                  ['grated-chocolate', 'pieces of chocolate', 'white chocolate glaze'],
                                  'sparkling chocolate', 'I love cho co\nla te ;Q', 'XXL'))
        Cake.bakery_offer.append(Cake('Meringue', 'meringue', 'cream', [],
                                  'vanilla', 'beZZa :p', 'M'))

    def info(self):
        print(25 * '-')
        print(self.name)
        print('Kind: {}'.format(self.kind))
        print('Carry taste: {}'.format(self.carry_taste))
        print('Additions: {}\nFilling: {}'.format(self.additions, self.filling))
        print('Some text: {}, Size: {}'.format(len(self.text) > 0, self.size))
        print(25 * '-')
        return self

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, list_additions: list):
        for x in list_additions:
            self.additions.append(x)


print('Today we offers:')
print(list(map(lambda cake: cake.name + ' and it\'s a ' + cake.kind, Cake.bakery_offer)))
# print(list(map(lambda cake: cake.name + '\nIt\'s a ' + (cake.kind + '\ '), bakery_offer)))
cake_02 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'S')
show_bakery_offer()
Cake.bakery_offer[-1].info()
Cake.bakery_offer[3].set_filling('2x vanilla')
Cake.bakery_offer[-1].add_additives(['whipped cream'])
Cake.bakery_offer[3].info()
Cake.bakery_offer[2].info()
Cake.bakery_offer.append(Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', '', 'S'))
Cake.bakery_offer[-1].info()

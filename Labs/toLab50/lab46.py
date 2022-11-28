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


class Cake:

    def __init__(self, name: str, kind: str, carry_taste: str, additions: list, filling: str,
                 text: str, size: str):
        self.name = name
        self.kind = kind
        self.carry_taste = carry_taste
        self.additions = additions
        self.filling = filling
        self.text = text
        self.size = size


cake_03 = Cake('Happy cake', 'sponge_cake', 'chocolate', ['icing-sugar', 'm&m', 'kitkat'],
               'cherry', 'Happy Day :)', 'L')
cake_04 = Cake('Fit cake', 'cheese_cake', 'carrot', ['banana', 'kiwi', 'nuts'],
               'nothing', 'I am fit because I like it! :)', 'M')
cake_05 = Cake('Chocko-power', 'chocolate_cake', 'chocolate',
               ['grated-chocolate', 'pieces of chocolate', 'white chocolate glaze'],
               'sparkling chocolate', 'I love cho co\nla te ;Q', 'XXL')

bakery_offer = [cake_03, cake_04, cake_05]

print('Today we offers:')
print(list(map(lambda cake: cake.name + ' and it\'s a ' + cake.kind, bakery_offer)))
# print(list(map(lambda cake: cake.name + '\nIt\'s a ' + cake.kind, bakery_offer)))

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



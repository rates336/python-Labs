import inspect
import os.path
import pickle
import glob
import types


def export_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Carry_taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additions</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    def export_one():
        content = template.format(obj.name, obj.kind, obj.carry_taste, obj.additions, obj.filling)
        f.write(content)

    def export_all():
        for z in obj.bakery_offer:
            content = template.format(z.name, z.kind, z.carry_taste, z.additions, z.filling)
            f.write(content)

    with open(path, 'w') as f:
        # if type_of_export == 'one':
        #     export_one()
        # elif type_of_export == 'all':
        #     export_all()
        # else:
        #     print('Wrong type_of_export')
        print(type(obj).__name__) # To understand in future !!!
        if inspect.isclass(obj):
            export_all()
        elif isinstance(obj, Cake):
            export_one()
        f.close()


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
        self.size = size
        self.__set_text(text)
        self.__gluten_free = __gluten_free
        Cake.bakery_offer.append(self)
        self.properties = [self.name, self.kind, self.carry_taste, self.additions, self.filling,
                           self.__text, self.size, self.__gluten_free]

    def info(self):
        print(25 * '-')
        print(self.name)
        print('Kind: {}'.format(self.kind))
        print('Carry taste: {}'.format(self.carry_taste))
        print('Additions: {}\nFilling: {}'.format(self.additions, self.filling))
        print('Some text: {}, Size: {}'.format(len(self.__text) > 0, self.size))
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

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.additions.count('frosting') > 0:
            self.__text = new_text
        else:
            print('Text can be only applied on type of glaze: {}'.format('frosting'))

    def save_to_file(self, path: str):
        with open(path, 'wb') as file:
            pickle.dump(self, file)
            file.close()

    @classmethod
    def read_from_file(cls, path: str):
        with open(path, 'rb') as file:
            cake_07 = pickle.load(file)
            cake_07.info()
            cake_07.set_filling('Strawberry jam')
            cls.bakery_offer.append(cake_07)

    @staticmethod
    def show_bakery_file(path: str):
        if path.endswith('\\'):
            print(glob.glob(path + '*'))
        else:
            print(glob.glob(path + '\\*'))

    Text = property(__get_text, __set_text, None, '__text')


Cake.bakery_offer.append(Cake('Happy cake', 'sponge', 'chocolate', ['icing-sugar', 'm&m', 'kitkat'],
                              'cherry', 'Happy Day :)', 'L'))
Cake.bakery_offer.append(Cake('Fit cake', 'cheese_cake', 'carrot', ['banana', 'kiwi', 'nuts'],
                              '', 'I am fit because I like it! :)', 'M'))
Cake.bakery_offer.append(Cake('Chocko-power', 'chocolate_cake', 'chocolate',
                              ['grated-chocolate', 'pieces of chocolate', 'white chocolate glaze'],
                              'sparkling chocolate', 'I love cho co\nla te ;Q', 'XXL'))
Cake.bakery_offer.append(Cake('Meringue', 'meringue', 'cream', [],
                              'vanilla', 'beZZa :p', 'M'))

Cake.export_cake_to_html = export_cake_to_html
Cake.export_all_cakes_to_html = types.MethodType(export_cake_to_html, Cake)
Cake.export_all_cakes_to_html('C:\\Python\\experiments\\exp\\lab48\\cake.html')
for x in Cake.bakery_offer:
    x.export_this_cake_to_html = types.MethodType(export_cake_to_html, x)

Cake.bakery_offer[2].export_this_cake_to_html('C:\\Python\\experiments\\exp\\lab48\\cake_02.html')

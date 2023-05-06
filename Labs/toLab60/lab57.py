# Class algorythm to refactor to create result how to course

class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product = 0
        self.current_promotion = 0
        self.current_customer = 0
        self.counter = 0

    def __getitem__(self, item):

        if item <= len(products) * len(promotions) * len(customers):
            ret = "{}, {}, {}".format(products[self.counter])

        else:
            raise StopIteration()


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

itr = iter(combinations)

print(next(itr))
print(next(itr))
print(next(itr))
# print(next(iter(next(itr))))

for x in combinations:
    print(x)







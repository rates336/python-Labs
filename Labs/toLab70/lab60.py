#To correct in free time

# def combinations_generator(products, promotions, customers):
#     current_customer = 0
#     current_promotion = 0
#     current_product = 0
#     len_products = len(products)
#     len_promotions = len(promotions)
#     len_customers = len(customers)
#
#     while True:
#         if current_product == len_products:
#             current_product = 0
#             current_promotion += 1
#             if current_promotion == len_promotions:
#                 current_promotion = 0
#                 current_customer += 1
#                 if current_customer == len_customers:
#                     break
#                 else:
#                     current_customer += 1
#             else:
#                 current_promotion += 1
#         else:
#             current_product += 1
#         item_to_return = "{} - {} -{}".format(products[current_product],
#                                               promotions[current_promotion],
#                                               customers[current_customer])
#
#         yield item_to_return
#
#
# products = ["Product {}".format(i) for i in range(1, 4)]
# promotions = ["Promotion {}".format(i) for i in range(1, 2)]
# customers = ['Customer {}'.format(i) for i in range(1, 5)]
#
# combinations = combinations_generator(products, promotions, customers)
#
# for c in combinations:
#     print(c)

# Other solotuion - to easier
def combinations(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield ("{} - {} - {}".format(i, j, k))


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for c in combinations(products, promotions, customers):
    print(c)
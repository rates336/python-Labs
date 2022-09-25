banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {}

for element in banknotes_coins:
    dict_denominations.setdefault(banknotes_coins, 0)
else:
    print('Finish adding elements to dictionary')


# def deposit_money(*money):
#     try:
#         money =
#     if 0 >= int(money):
#         print('For deposit you will give money to deposit')
#         return

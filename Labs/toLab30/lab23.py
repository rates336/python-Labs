from geometric import *


print(give_geom_seq_element(1, 2, 64))
print(give_geom_seq_element(3, 2, 10, True))
print(give_factor_for_geom_seq(12, 24))
print(give_factor_for_geom_seq(12, 24, 9))
print(give_factor_for_geom_seq(12, 24, 9, return_tab_numbers=True))
print(give_factor_for_geom_seq(12, 24, 9, 1, return_tab_numbers=True))
print(give_factor_for_geom_seq(12, 24, 4, 3, False, True))
print(give_factor_for_geom_seq(12, 24, 4, 0, False, True))
print(give_factor_for_geom_seq(12, 24, 4, 7, False, True, True))
print(geo_square_function(1, c=9, x=193))
print(geo_square_function(1, 3, 9, True, x=3))
print(geo_square_function(1, 3, 9, True, True, 3))
print(geo_square_function(1, 3, 9, False, x=3))
print(geo_square_function(5, 4, 1, False, True, 0))

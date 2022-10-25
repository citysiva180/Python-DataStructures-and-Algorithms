# Names Tuple

import collections
from collections import namedtuple

point = namedtuple('point', 'x,y,z')
new_point = point(3, 4, 5)
print(new_point)

cars = namedtuple('prime', ["sedan", "coupe", "four", "sports"])
prime_cars = cars("BMW", "Mercedes", "Subaru", "Koneigsagg")
print(prime_cars)

celebrity_dict = namedtuple(
    'a_list', {'new_face': "", 'singer': "", 'queen_bey': ""})
a_list_celebs = celebrity_dict('Bradly Cooper', 'Lady Gaga', 'Beyonce')
print(a_list_celebs.new_face, a_list_celebs.singer, a_list_celebs.queen_bey)
print(a_list_celebs._fields)
new_celeb_list = a_list_celebs._replace(new_face='Tom Cruise')
print(new_celeb_list)

p2 = a_list_celebs._make(['Ninja Turtles', 'Nicki Minaj', 'Solange'])
print(p2)

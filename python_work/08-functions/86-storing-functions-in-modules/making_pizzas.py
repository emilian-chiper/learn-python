# Importing a Module
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'prosciuto', 'mozarella')

# Importing a Function from a Module
# from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'prosciouto', 'pesto genovese')

# Using as to Give a Function an Alias
# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'prosciouto', 'pesto genovese')

# Using as to Give a Module an Alias
# import pizza as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'prosciouto', 'pesto genovese')

# Import All Functions in a Module
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'prosciouto', 'pesto genovese')

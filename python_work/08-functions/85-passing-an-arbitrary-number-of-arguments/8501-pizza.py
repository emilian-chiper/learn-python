# PASSING AN ARBITRARY NUMBER OF ARGUMENTS

# def make_pizza(*toppings) # * creates an empty tuple
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"\t- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MIXING POSITIONAL AN ARBITRARY ARGUMENTS
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'musshrooms', 'green peppers', 'extra cheese')
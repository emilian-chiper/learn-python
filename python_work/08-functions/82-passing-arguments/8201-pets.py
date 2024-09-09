# # Positional Arguments
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamester', 'harry')

# Multiple function calls
# describe_pet('dog', 'arrow')
# describe_pet('cat', 'josephine')

# Order matters
# describe_pet('harry', 'hamster')

# Keyword Arguments
# describe_pet(animal_type='hamster', pet_name='harry')

# Order can be controlled with keyword args
# describe_pet(pet_name='arrow', animal_type='dog')

# Default Values
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name='willie')

# Prof
# describe_pet('willie')

# To describe an animal other than a dog
# describe_pet(pet_name='harry', animal_type='hamster')

# Equivalent Function Calls
# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie
# describe_pet('willie')
# describe_pet(pet_name='willie')

# A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding Argument Errors
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet() # TypeError: describe_pet() missing 1 required positional arguments
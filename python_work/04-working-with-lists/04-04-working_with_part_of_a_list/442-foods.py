# Copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# The lists are separate
# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print('\n')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# Copying without slice
my_foods = ['pizza', 'falafel', 'carrot cake']

# This isn't a copy, it's another pointer to the same object in memory
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\n')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
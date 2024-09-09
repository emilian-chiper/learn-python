# age = 4
# stage = ''

# if age < 2:
#     stage = 'baby'
# elif age >= 2 and age < 4:
#     stage = 'toddler'
# elif age >= 4 and age < 13:
#     stage = 'kid'
# elif age >= 13 and age < 20:
#     stage = 'teenager'
# elif age >=20 and age < 65:
#     stage = 'adult'
# else:
#     stage = 'elder'

# print(f"This person is {age} years old, which makes them an {stage}.")

# Removing redundancy
age = 65
stage = ''

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"This person is {age} years old, which makes them an {stage}.")
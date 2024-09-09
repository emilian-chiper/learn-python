# Using int() to Accept Numerical Input
age = input("How old are you? ")
# print(age >= 18) # TypeError: unorderable types: str() >= int()
age = int(age)

print(age)
print(age >= 18)

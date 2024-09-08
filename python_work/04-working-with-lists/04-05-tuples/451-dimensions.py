# Defining a tuple
dimensions = (200, 5)

print(dimensions[0])
print(dimensions[1])

# Changing an item
# dimension[0] = 250 # TypeError: 'tuple' object does not support item assignment

# Looping through all values in a tuple
for dimension in dimensions:
	print(dimension)

# Writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
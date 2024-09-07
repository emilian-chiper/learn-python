cars = ['bmw', 'audi', 'toyota', 'subaru']

# Sorting
cars.sort()
print(cars)

# Sorting in reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sort temporarily (doesn't mutate the list)
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(f"Here is the original list:\n{cars}")

print(f"\nHere is the sorted list:\n\t{sorted(cars)}")

print(f"Here is the original list again:\n{cars}")

# Printing a list in reverse order (i.e. reverse indexing)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
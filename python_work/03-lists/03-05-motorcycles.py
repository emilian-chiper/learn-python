motrocycles = ['honda', 'yamaha', 'suzuki']
print(motrocycles)

# Modifying elements in a list
motrocycles[0] = 'ducati'
print(motrocycles)

# Appending
motrocycles.append('ducati')
print(motrocycles)

motrocycles = []

motrocycles.append('honda')
motrocycles.append('yamaha')
motrocycles.append('suzuki')

print(motrocycles)

# Inserting
motrocycles = ['honda', 'yamaha', 'suzuki']

motrocycles.insert(0, 'ducati')
print(motrocycles)

# Removing
motrocycles = ['honda', 'yamaha', 'suzuki']
print(motrocycles)

# del
del motrocycles[1]
print(motrocycles)

# pop()
motrocycles = ['honda', 'yamaha', 'suzuki']
print(motrocycles)

popped_motorcycle = motrocycles.pop()
print(motrocycles)
print(popped_motorcycle)

motrocycles = ['honda', 'yamaha', 'suzuki']

last_owned = motrocycles.pop()
print(f"The last motrocycles I owned was a {last_owned.title()}")

# pop() at any index
motrocycles = ['honda', 'yamaha', 'suzuki']

first_owned = motrocycles.pop(0)
print(f"The first motrocycle I owned was a {first_owned.title()}.")

# Remove an item by value
motrocycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motrocycles)

too_expensive = 'ducati'
motrocycles.remove(too_expensive)
print(motrocycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

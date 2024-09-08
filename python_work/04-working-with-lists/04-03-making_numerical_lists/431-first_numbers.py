# range()
for value in range(1, 5):
	print(value) # 1, 2, 3, 4 <-- this is the 'off by one' rule in application

print("\n")

for value in range(1, 6):
	print(value)

print("\n")

# Use range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
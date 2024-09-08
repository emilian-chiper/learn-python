cities = ['bucharest', 'rome', 'paris', 'new york', 'kyoto', 'seoul']
print(cities)

cities.insert(0, 'moscow')
print(cities)

cities.append('berlin')
print(cities)

del cities[1]
print(cities)

cities.pop()
print(cities)

cities.pop(3)
print(cities)

too_far = 'seoul'
cities.remove(too_far)
print(cities)

print(sorted(cities))

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)

print(len(cities))
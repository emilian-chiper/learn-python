# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4]) # in fact [1:4)
print(players[:4]) # in fact [:4)
print(players[2:])
print(players[-3:]) # in fact (-3:]

# Looping through a slice
print("Here are the first three players of my team:")
for player in players[:3]:
	print(player.title())
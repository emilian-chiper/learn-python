my_pizzas = ['margherita', 'alla grigia', 'diavola']
friend_pizzas = my_pizzas[:]

my_pizzas.append('con carne')
friend_pizzas.append('deep dish')

print(f"My favorite pizzas are: {', '.join(my_pizzas)}.")
print(f"My friend's favorite pizzas are: {', '.join(friend_pizzas)}.")
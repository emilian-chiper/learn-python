car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru') # True

print("\nIs car == 'audi'? I predict False")
print(car == 'audi') # False

print("\nIs car == 'Audi'? I predict False")
print(car == 'Audi') # False

print("\nIs car == 'Subaru'? I predict False")
print(car == 'Subaru') # False

print("\nWhat about car.title()? I predict True")
print(car.title() == 'Subaru') # True

print("\nLet's try something a lil' different.")

print("\nIs car <= 'Subaru'? I predict False")
print(car <= 'Subaru') # False

print("\nWhat about the opposite? I predict True")
print(car >= 'Subaru') # True <-- s > S (unicode juju)

print("\nLet's look at a negation. I predict True")
print(car != 'Subaru') # True

print("\nNow let's do some numbers")
num = 22

print("\nIs num greater than infinity? I predict False")
print(num > float('inf')) # False

print("\nIs then num smaller than infinity and greater than 22? I predict False")
print(num < float('inf') and num > 22) # False

print("\nIs then num smaller than infinity or larger than 22? I say True")
print(num < float('inf') or num > 22) # True

print("\nIs num smaller than car? I predict Sy")
# print(num < car) # Oh no, a TypeError

print("\nNow let's work lists")
cars = ['toyota', 'honda', 'suzuki', 'ford']

print("\n")

if car in cars:
    print(f"Out of this selection, {car} is a decent choice.")
elif car not in cars:
    print(f"We're sorry but {car} isn't part of our selection.")

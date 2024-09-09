responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'yes' or repeat == 'y':
        continue
    elif repeat == 'no' or repeat == 'n':
        active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
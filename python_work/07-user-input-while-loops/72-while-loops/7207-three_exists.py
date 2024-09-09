prompt = "\nTell me what toppings you'd like:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    topping = input(prompt)

    if topping == '':
        active = False
    elif topping == 'quit':
        break
    else:
        print(f"\nAdded {topping} to your pizza.")
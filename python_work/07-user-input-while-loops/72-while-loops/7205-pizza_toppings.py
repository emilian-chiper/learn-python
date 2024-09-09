prompt = "\nTell me what toppings you'd like:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"\nAdded {topping} to your pizza.")
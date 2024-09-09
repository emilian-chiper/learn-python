prompt = "What's your age? "

while True:
    age = int(input(prompt))

    output = ''

    if age < 3:
        output = f"You're {age} years old. The ticket is free."
    elif age < 12:
        output = f"You're {age} years old. The ticket is $10."
    else:
        output = f"You're over {age}. That'll be $12, old man."

    print(output)
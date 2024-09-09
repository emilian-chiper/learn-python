favourite_numbers = {
    'james': [24, 1231, 76],
    'lia': [69, 98417, 22, 975],
    'hans': [88, 1349, 1203],
    'valery': [666, 420, 92746],
    'pip': [2, 3, 4]
}

for name, nums in favourite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: {', '.join(map(str, nums))}.")
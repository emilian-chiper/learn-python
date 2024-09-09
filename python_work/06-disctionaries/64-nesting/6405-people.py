people = [
    {
        "first_name": "jon",
        "last_name": "snow",
        "age": 18,
        "city": "winterfell"
    },
    {
        "first_name": "tyrion",
        "last_name": "lannister",
        "age": 35,
        "city": "lannisport",
    },
    {
        "first_name": "rhaenyra",
        "last_name": "targaryen",
        "age": 34,
        "city": "dragonstone",
    }
]

for item in people:
    print(f"This is {item["first_name"].title()} {item["last_name"].title()}, they're {item["age"]} years old and currently live at {item["city"].title()}.")

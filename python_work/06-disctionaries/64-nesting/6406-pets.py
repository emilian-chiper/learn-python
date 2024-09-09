pets = [
    {
        "name": "white fang",
        "species": "dog",
        "owner": "bob",
    },
    {
        "name": "edith",
        "species": "cat",
        "owner": "sarah",
    },
    {
        "name": "ivan",
        "species": "bear",
        "owner": "ivan",
    }
]

for pet in pets:
    print(f"{pet["name"]} is a {pet["species"]}, and its owner is {pet["owner"]}")
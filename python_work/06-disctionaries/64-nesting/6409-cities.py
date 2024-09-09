cities = {
    "paris": {
        "country": "france",
        "population": 2_161_000,
        "fact": "it was the first city to implement torch electricity lamps",
    },
    "london": {
        "country": "united kingdom",
        "population": 8_982_000,
        "fact": "it stinks",
    },
    "rome": {
        "country": "Italy",
        "population": 2_873_000,
        "fact": "it is eternal"
    },
}

for city, info in cities.items():
    print(f"City: {city.title()}")
    for key, value in info.items():
        if key == "country":
            print(f"\t{key.title()}: {value.title()}")
        else:
            print(f"\t{key.title()}: {value}")
    print("\n")
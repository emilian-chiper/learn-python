rivers = {
    "nile": "egypt",
    "danube": "austria",
    "volga": "russia",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")
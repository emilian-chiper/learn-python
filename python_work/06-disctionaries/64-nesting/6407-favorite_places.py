favorite_places = {
    "jon": ['paris'],
    "anne": ['london', 'grene gables'],
    "steve": ['murica', 'brasil', 'vietnam'],
}

for name, places in favorite_places.items():
    print(f"{name.title()} enjoys:")
    for place in places:
        print(f"\t{place.title()}")
def describe_city(city, country='italy'):
    """Prints info about the capital of a country"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("rome")
describe_city("paris", "france")
describe_city("moscow")
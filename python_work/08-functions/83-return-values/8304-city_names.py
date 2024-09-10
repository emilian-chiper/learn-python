def city_country(city, country):
    """Returns the names of city and country"""
    cityCountry = f"{city}, {country}"
    return cityCountry.title()

print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('rome', 'italy'))
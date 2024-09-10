def make_car(manufacturer, model_name, **car_options):
    """
    Receives a manufacturer, model name, and options.
    Builds a dictionary.
    Returns dictionary.
    """
    car_options["manufacturer"] = manufacturer
    car_options["model_name"] = model_name
    return car_options

car_1 = make_car('bmw', 'x6', color='black', engine="4.4 L")
car_2 = make_car('volvo', 'xc40', color='silver', traction='back')
car_3 = make_car('nissan', 'murano', color='red', max_seats="5")

print(f"{car_1}\n{car_2}\n{car_3}")
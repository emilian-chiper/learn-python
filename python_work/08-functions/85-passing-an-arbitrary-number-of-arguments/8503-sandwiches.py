def make_sandwiches(*fillings):
    """
    Collects as many items as specified in the call.
    Prints a summary of the sandwich.
    """
    print("Making a sandwich with the following fillings:")
    for filling in fillings:
        print(f"\t- {filling}")

make_sandwiches('salami')
make_sandwiches('tomato', 'mozarrella')
make_sandwiches('salad', 'fries', 'chicken nuggies')
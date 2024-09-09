def make_shirt(size='L', text='I love Python'):
    """Prints the size of the shirt and the message"""
    print(f"\nThis shirt is size {size}.")
    print(f"On the front, the writing sais {text.title()}.")

make_shirt()
make_shirt('M')
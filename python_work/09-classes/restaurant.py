# RESTAURANT CLASS

class Restaurant():
	"""Prints a message indicating that the restaurant is open"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print(self.restaurant_name.title())
		print(self.cuisine_type.title())
		
	def open_restaurant(self):
		print(f"{self.restaurant_name.title()} is open!")

le_reuvage = Restaurant('le reuvage', 'french')
le_reuvage.describe_restaurant()
le_reuvage.open_restaurant()

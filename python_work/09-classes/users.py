"""
The user class
"""
class User():
	"""Describes and greets people"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		
	def describe_user(self):
		"""Describes a user"""
		print(f"{self.first_name.title()} {self.last_name.title()} is our newest user.")
		
	def greet_user(self):
		user = f"{self.first_name.title()} {self.last_name.title()}!"
		print(f"Hey there, {user}")
		
user_1 = User("jimi", "hendrix")
user_2 = User("freddie", "mercury")
user_3 = User("john", "bonham")

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

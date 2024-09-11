# Creating the DOG class

class Dog():
	"""A simple attempt to mode a dog."""
	
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")
		
# Making an instance from a class
my_dog = Dog('willie', 6)

# ~ print("My dog's name is " + my_dog.name.title() + ".")
# ~ print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

# Creating Multiple instances
my_dog = Dog('butcher', 7)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sti()



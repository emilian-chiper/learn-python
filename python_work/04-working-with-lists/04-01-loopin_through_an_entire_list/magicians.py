magicians = ['alice', 'david', 'carolina']

# The for loop
for magician in magicians:
	print(magician)

# Doing More Work Within a for Loop
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
	
	# Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")
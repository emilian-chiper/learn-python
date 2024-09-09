question = input("How many seats do you need? ")
answer = int(question)

seating = ""
if answer > 8:
    seating = "We're sorry, but you'll have to wait for a table."
else:
    seating = "Your table is ready!"

print(seating)
alien_color = 'yellow'

# if alien_color == 'green':
#     print("You earned 5 points for shooting the alien.")
# elif alien_color == "yellow":
#     print("You earned 10 points for shooting the alien.")
# else:
#     print("You earned 15 points for shooting the alien.")

# But since the above doesn't respect DRY
points = 0;

if alien_color == 'green':
    points = 5
elif alien_color == "yellow":
    points = 10
else:
    points = 15

print(f"You earned {points} points for shooting the alien.")
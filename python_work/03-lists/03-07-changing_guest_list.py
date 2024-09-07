guest_list = ['socrates', 'kassandra', 'guga']

print(f"Esteemed {guest_list[0].title()}, would you join me for dinner?")
print(f"Dear {guest_list[1].title()}, how abbout dinner?")
print(f"{guest_list[2].title()}, bro, join me for dinner.")

print(f"{guest_list[0].title()} won't make it, unfortunately...")

guest_list[0] = 'lord toranaga'

print(f"Esteemed {guest_list[0].title()}, would you join me for dinner?")
print(f"Dear {guest_list[1].title()}, how abbout dinner?")
print(f"{guest_list[2].title()}, bro, join me for dinner.")
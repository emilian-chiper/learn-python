guest_list = ['socrates', 'kassandra', 'guga']

print(f"Esteemed {guest_list[0].title()}, would you join me for dinner?")
print(f"Dear {guest_list[1].title()}, how abbout dinner?")
print(f"{guest_list[2].title()}, bro, join me for dinner.")

print(f"{guest_list[0].title()} won't make it, unfortunately...")

guest_list[0] = 'lord toranaga'

print(f"Esteemed {guest_list[0].title()}, would you join me for dinner?")
print(f"Dear {guest_list[1].title()}, how abbout dinner?")
print(f"{guest_list[2].title()}, bro, join me for dinner.")

print("Looks like we founda bigger table.")

guest_list.insert(0, 'balthasar gelt')
guest_list.insert(2, 'hypathia')
guest_list.append('salvador dali')

print(f"Patriarch {guest_list[0].title()}, would you join me for dinner?")
print(f"Esteemed {guest_list[1].title()}, how abbout dinner?")
print(f"{guest_list[2].title()}, join me for dinner.")
print(f"Dear {guest_list[3].title()}, it's time for dinner.")
print(f"{guest_list[4].title()}, bro, let's make dinner. Steak, right?")

print(f"Unfortunately, there appears to only be room left for two.")

print(f"{guest_list.pop().title()}, I'm sorry, but I can't have you for dinner")
print(f"{guest_list.pop().title()}, I'm sorry, but I can't have you for dinner")
print(f"{guest_list.pop().title()}, I'm sorry, but I can't have you for dinner")
print(f"{guest_list.pop().title()}, I'm sorry, but I can't have you for dinner")

print(f"{guest_list[0].title()}, {guest_list[1].title()}, you're still invited.")

del guest_list[1]
del	guest_list[0]

print(guest_list)

current_users = ['Boblin', 'Sara', 'Dan', 'Admin', 'Pod']
new_users = ['sara', 'Haxor', 'Dan', 'Poppins', 'Tatiana']
current_users_lower = [name.lower() for name in current_users[:]]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.title()} is already taken. Please choose another.")
    else:
        print(f"{new_user.title()} is an available name.")
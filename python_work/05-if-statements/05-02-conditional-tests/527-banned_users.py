# Checking whether a value is NOT in a list
banned_users = ['andre', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a reply if you wish.")
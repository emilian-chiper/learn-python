favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# Looping through all keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
    
# Another example
friends = ['phil', 'sarah'] # Array containing friend's names
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}!")

    if name in friends: # if a key is also in the friends array
        # Set language to the value at position (key) name and capitalize
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Looping through a dict's keys in a particular order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

subjects = ['dan', 'phil', 'marcela', 'sarah', 'stephen', 'weili']

for subject in subjects:
    if subject in favorite_languages.keys():
        print(f"Thanks for taking the poll, {subject.title()}.")
    else:
        print(f"Hey {subject.title()}, please take this poll!")

    
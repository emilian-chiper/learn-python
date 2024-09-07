bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']

# Accessing elements
print(bicycles[0]) # trek

# Index positions start at 0, not at 1
print(bicycles[1]) # cannondale
print(bicycles[3]) # specialized
print(bicycles[-1]) # specialized

# Using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message) # My first bicycle was a Trek.
nums = [num for num in range(1, 10)]
suffix = ''

for num in nums:
    if num == 1:
        suffix = 'st'
    elif num == 2:
        suffix = 'nd'
    elif num == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(f"{num}{suffix}")
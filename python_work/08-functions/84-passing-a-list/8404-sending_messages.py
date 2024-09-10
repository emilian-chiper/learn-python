messages = ['this', 'is', 'a', 'list', 'of', 'short', 'messages']
sent_messages = []

# def show_messages(arr):
#     """Iterates through a list and prints its elements"""
#     for el in arr:
#         print(el)

def send_messages(arr_1, arr_2):
    """
    Iterates through a list.
    While it iterates, it prints the elements.
    As the messages are printed, they are moved to a second empty list.
    Finally, both lists are printed.
    """
    print(f"messages: {arr_1}")
    print(f"sent messages: {arr_2}")
    
    while arr_1:
        for el in arr_1:
            curr_el = arr_1.pop()
            print(curr_el)
            arr_2.append(curr_el)
    print(f"messages: {arr_1}")
    print(f"sent messages: {arr_2}")

send_messages(messages, sent_messages)

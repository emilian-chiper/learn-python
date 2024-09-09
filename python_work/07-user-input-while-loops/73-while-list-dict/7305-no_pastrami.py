sandwich_orders = ['cubano', 'pastrami', 'banh mi', 'pastrami', 'bauru', 'pastrami', 'gyro', 'kumru']
finished_sandwiches = []

print("We're sorry, but we're out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
    print(f"I made your {order.title()} sandwich.")

print("\nAll sandwiches completed:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
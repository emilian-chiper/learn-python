sandwich_orders = ['cubano', 'banh mi', 'bauru', 'gyro', 'kumru']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_sandwiches.append(order)
    print(f"I made your {order.title()} sandwich.")

print("\nAll sandwiches completed:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
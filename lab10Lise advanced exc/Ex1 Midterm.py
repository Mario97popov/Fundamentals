count_orders = int(input())

tp = 0

for numbers in range(0, count_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = ((days * capsule_count) * price_per_capsule)
    tp += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${tp:.2f}")

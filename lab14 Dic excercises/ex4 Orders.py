products_prices = {}
products_quantities = {}
data = input()

while not data == "buy":
    product, price, quantity = data.split(" ")
    quantity = int(quantity)
    price = float(price)
    if product not in products_prices:
        products_prices[product] = price
        products_quantities[product] = quantity
    else:
        products_prices[product] = price
        products_quantities[product] += quantity

    data = input()

for product, price in products_prices.items():
    total = price * products_quantities[product]
    print(f"{product} -> {total:.2f}")

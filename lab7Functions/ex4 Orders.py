def total_price(product, num):
    result = 0
    if product == "coffee":
        result = num * 1.5
    elif product == "water":
        result = num * 1.00
    elif product == "coke":
        result = num * 1.40
    elif product == "snacks":
        result = num * 2.00
    return result


item = input()
quantity = float(input())
print(f"{total_price(item, quantity):.2f}")

data = input().split()
products = {}
for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

products_searched = input().split(" ")
for product in products_searched:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

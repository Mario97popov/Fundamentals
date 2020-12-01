type_metal = input()

inventory = {}

while not type_metal == "stop":
    quantity = int(input())
    if type_metal in inventory:
        inventory[type_metal] += quantity
    else:
        inventory[type_metal] = quantity
    type_metal = input()

for key, value in inventory.items():
    print(f"{key} -> {value}")

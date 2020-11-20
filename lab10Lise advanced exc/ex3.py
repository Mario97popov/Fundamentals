owned_cards = input().split(", ")
numbers = int(input())

while numbers:
    commands = input().split(", ")
    command = commands[0]
    if len(command) > 6:
        index = int(commands[1])
        if index in range(0, len(owned_cards)):
            owned_cards.remove(owned_cards[index])
            print("Card successfully sold")
        else:
            print("Index out of range")

    elif command == "Add":
        car = commands[1]
        if car in owned_cards:
            print("Card is already bought")
        else:
            print("Card successfully bought")
            owned_cards.append(car)
    elif command == "Remove":
        car = commands[1]
        if car in owned_cards:
            print("Card successfully sold")
            owned_cards.remove(car)
        else:
            print("Card not found")
    elif command == "Insert":
        index = int(commands[1])
        car = commands[2]
        if not (index in range(0, len(owned_cards))) and not (car in owned_cards):
            print("Index out of range")
        elif (index in range(0, len(owned_cards))) and not (car in owned_cards):
            owned_cards.insert(index, car)
            print("Card successfully bought")
        elif (index in range(0, len(owned_cards))) and (car in owned_cards):
            print("Card is already bought")

    numbers -= 1

print(f"{', '.join(owned_cards)}")
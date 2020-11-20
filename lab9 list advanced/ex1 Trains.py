numbers_of_wagons = int(input())

train = [0 for iter in range(numbers_of_wagons)]

command = input()

while not command == "End":
    data = command.split()

if data[0] == "add":
    numbers_of_people = int(data[1])
    train[-1] += numbers_of_people
elif data[0] == "insert":
    index = int(data[1])
    numbers_of_people = int(data[2])
    train[index] += numbers_of_people
elif data[0] == "leave":
    index = int(data[1])
    numbers_of_people = int(data[2])
    train[index] -= numbers_of_people

command = input()

print(train)

numbers = input().split(' ')
# lol = [int(el) for el in numbers]
numbers.sort(reverse=True)
lol = [int(el) for el in numbers]
for i in lol:
    print(i, end= '')



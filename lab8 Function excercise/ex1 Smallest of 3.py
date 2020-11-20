def smallest(num1, num2, num3):
    if num1 < num2 and num3:
        return num1
    elif num3 < num2 and num1:
        return num3
    elif num2 < num1 and num3:
        return num2


numb_1 = int(input())
numb_2 = int(input())
numb_3 = int(input())

print(smallest(numb_1, numb_2, numb_3))
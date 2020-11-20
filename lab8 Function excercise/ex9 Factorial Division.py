def factorial_division(n):
    res = 1
    for num in range(1, n + 1):
        res *= num

    return res


number = int(input())
number_2 = int(input())
factorial_number_1 = factorial_division(number)
factorial_number_2 = factorial_division(number_2)
result = factorial_number_1/factorial_number_2
print(f"{result:.2f}")
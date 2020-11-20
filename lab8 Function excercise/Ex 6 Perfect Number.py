def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if Number % i == 0:
            Sum = Sum + i
    return Sum


Number = int(input())
if Number == Perfect_Number(Number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

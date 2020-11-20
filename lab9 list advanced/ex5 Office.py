arr = [int(el) for el in input().split(",")]

arrResult = []

for index in arr:
    indecies = [index, index]
    indecies_2 = [-index, -index]
    if index > 0:
        lol = sum(arr[i] for i in indecies)
        arrResult.append(lol)
    elif index < 0:
        kek = sum(arr[i] for i in indecies_2)
        arrResult.append(kek)
    elif index == 0:
        arrResult.append(0)

    # elif index < 0:

print(arr)
print(arrResult)

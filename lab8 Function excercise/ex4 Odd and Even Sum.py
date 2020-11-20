def single_num(num):
    num_in_string = str(num)
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_in_string)):
        lol = int(num_in_string[i])
        if lol % 2 == 0:
            even_sum += lol
        elif lol % 1 == 0:
            odd_sum += lol
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
    return even_sum and odd_sum


number = int(input())
single_num(number)

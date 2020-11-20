def convert_to_int(el):
    return int(el)


lambda el: int(el) ** 2

nums_as_string = [1, 2, 3]
# numbers = [int(el) for el in nums_as_string]
# numbers = [convert_to_int(el) for el in nums_as_string]
# numbers = list(map(int, nums_as_string))
# numbers = list(map(lambda el: int(el), nums_as_string))
# evens = [el for el in nums_as_string if el % 2 == 0]
evens = list(filter(lambda x: x % 2 == 0, nums_as_string))
print(evens)

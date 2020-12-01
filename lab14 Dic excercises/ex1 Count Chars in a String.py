str1 = input()

my_dict = {}
for n in str1:
    keys = my_dict.keys()
    if n != " ":
        if n in keys:
            my_dict[n] += 1
        else:
            my_dict[n] = 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")

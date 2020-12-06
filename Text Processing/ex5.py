letters = []
digits = []
others = []

line = input()

for char in line:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        others += char

print(digits)
print(letters)
print(others)
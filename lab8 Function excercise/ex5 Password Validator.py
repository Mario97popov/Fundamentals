import re


def validator_password(password):
    is_valid = True
    if not len(password) >= 6 or len(password) >= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    pattern = "^[A-Za-z0-9_]*$"
    if not bool(re.match(pattern, password)):
        is_valid = False
        print("Password must consist only of letters and digits")
    if sum(map(str.isdigit, password)) < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    return is_valid
    # else:
    #     print("Password is valid")


lol = input()
is_valid = validator_password(lol)
if is_valid:
    print("Password is valid")

substrings = input().split(", ")
words = input().split(', ')

result = [subst for word in words for subst in substrings if subst in word]

print(sorted(set(result), key=result.index))
# for word in words:
#     for subst in substrings:
#         if subst in word and not subst in result:
#             result.append(subst)

# for substrings[i] in any_strings[i]:
#     if substrings[i] == any_strings:

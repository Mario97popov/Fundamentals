banned_words = input().split(", ")
text = input()

for banned_word in banned_words:
    text = text.replace(banned_words, "*" * len(banned_word))

print(text)
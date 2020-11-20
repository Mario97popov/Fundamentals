def char_in_range(char1, char2):
    single = ''
    for n in range(chr(char1), chr(char2)):
        single += n
        return single


char_1 = input()
char_2 = input()
print(char_in_range(char_1,char_2))

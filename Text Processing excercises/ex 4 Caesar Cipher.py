def caesar(plain_Text, shift):
    cipher_Text = ""
    for ch in plain_Text:
        if ch.isalpha():
            stayIn_Alphabet = ord(ch) + shift
            if stayIn_Alphabet > ord('z'):
                stayIn_Alphabet -= 26
            final_Letter = chr(stayIn_Alphabet)
            cipher_Text += final_Letter
    print(cipher_Text)
    return cipher_Text


plainText = input()
shift = 3
caesar(plainText, shift)

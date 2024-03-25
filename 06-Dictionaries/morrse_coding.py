from morsecode import morse 

word = input("Your word: ")

morse_word = ""
for char in word.upper():
    if char == " ":
        morse_word += "   "
    else:
        if char not in morse:
            continue          # continue with next char, go back to for
        morse_word += morse[char] + " "

print(morse_word)

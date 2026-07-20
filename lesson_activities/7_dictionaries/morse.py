#=======================
# TODO
# Implement morseToAlpha
# It should translate a string of morse code into the roman alphabet
# Here is the format for the morse_string:
#   dots are represented with .
#   dashes are represented with -
#   there is a blank space ' ' between each letter
#   there is a forward slash / between each word
# See main() for some examples

def morseToAlpha(morse_string):
    pass


#=======================



def main():
    test_string = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    print(morseToAlpha(test_string)) # 'hello world'

    test_string = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    print(morseToAlpha(test_string)) # the alphabet

if __name__ == "__main__":
    main()
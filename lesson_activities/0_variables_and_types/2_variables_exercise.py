# Variables Exercise
#=======================
# TODO
# First, create a variable named 'one_word' and assign the literal str "no" to it
# Next, create a variable named 'five_words' and assign to it the text "nonononono" (five repetitions), but WITHOUT using a str literal
# Use your 'one_word' variable and one or more string operations.
# Finally, replace the value stored in 'one_word' with the literal "yes"



#=======================

print("")
if not (type(one_word) == type(five_words) and type(one_word) == type(str())):
    print("Variable types are incorrect.\n")
    exit()

if not (five_words == "nonononono" and one_word == "yes"):
    print("Values stored in variables are incorrect.\n")
    exit()
print("Success.\n")
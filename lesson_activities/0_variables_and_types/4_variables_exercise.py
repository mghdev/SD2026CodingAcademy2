# Variables Exercise
#=======================
# TODO
# Create a variable named 'temp' and assign a str literal to it with length 7, the character 'g' at index 1, and a digit at index 3
# Create a variable named 'just_one' and assign to it the single character at index 5 in 'temp'
# Create a variable named 'shorty' and assign an expression that calculates the length of 'temp' minus 4



#=======================

print("")
if not (type(temp) == type(just_one) and type(temp) == type(str()) and type(shorty) == type(int())):
    print("Variable types are incorrect.\n")
    exit()

if not (len(temp) == 7 and temp[1] == "g" and str.isdigit(temp[3]) and just_one == temp[5] and shorty == 3):
    print("Values stored in variables are incorrect.\n")
    exit()
print("Success.\n")
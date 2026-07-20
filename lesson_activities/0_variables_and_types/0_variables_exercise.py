# Variables Exercise
#=======================
# TODO
# Create a variable named 'cats' and assign the literal 21 to it
# Create a variable named 'dogs' and assign 9 to it
# Create a variable named 'honey_badger' and assign 1 to it



#=======================



print("")
if not (type(cats) == type(dogs) and type(honey_badger) == type(dogs) and type(cats) == type(int())):
    print("Variable types are incorrect.\n")
    exit()

if not (cats == 21 and dogs == 9 and honey_badger == 1):
    print("Values stored in variables are incorrect.\n")
    exit()

print("Success.\n")
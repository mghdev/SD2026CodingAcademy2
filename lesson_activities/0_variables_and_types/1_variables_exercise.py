# Variables Exercise
#=======================
# TODO
# Create a variable called 'intermediate' and assign 9.0 to it
# Create a variable 'x1' and assign the square-root of 'intermediate' to it
# Create a variable 'x2' and assign the inverse of 1+intermediate to it  ( "one-divided-by-(intermediate-plus-one)" )



#=======================

print("")
if not (type(intermediate) == type(x1) and type(x1) == type(x2) and type(x1) == type(float())):
    print("Variable types are incorrect.\n")
    exit()

if not (intermediate == 9.0 and x1 == 3.0 and x2 == 0.1):
    print("Values stored in variables are incorrect.\n")
    exit()
print("Success.\n")
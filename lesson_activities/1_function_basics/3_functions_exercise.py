# Funtions Exercise
#=======================
# TODO
# Define a function named 'addFive' with one parameter named 'number'.
# addFive should return the result of adding 5 to its 'number' parameter.
# Call addFive with an argument of your choice and print the return value.
# Always run your code!



#=======================



def testAddFive(num):
    target = num + 5
    result = addFive(num)
    if not (result == target):
        print("addFive(",num,") should have returned ",target,", but instead it returned ",result,".",sep="")
        exit()

print()
testAddFive(2)
testAddFive(-4)
testAddFive(3.4)
testAddFive(28.0)
print("Success.\n")
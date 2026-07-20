#=======================
# TODO
# The function 'solveQuadratic' takes 3 parameters 'a', 'b', and 'c' that are the coefficients of a quadratic equation of the form
#   ax^2 + bx + c = 0
# It should return the two solutions to the equation given by its arguments.
# For example, the call 'solveQuadratic(1,-2,1)' should return 1,1
# Complete the body of the function so that it assigns expressions to the variables x1 and x2 that will evaluate to the correct solutions.
# It may be helpful to define an intermediate variable to store a value that appears in both expressions.

def solveQuadratic(a,b,c):
    d = 0
    x1 = 0
    x2 = 0
    return x1,x2


# Pre-made test case
x1,x2 = solveQuadratic(1,-2,1)
if not (x1 == 1 and x2 == 1):
    print("Incorrect results for 'solveQuadratic(1,-2,1)'. Returned",x1,"and",x2,"instead of the correct values.")


#=======================
# TODO
# Make up a quadratic equation as a test case for your function.
# Call solveQuadratic with the right arguments for your test case and print the return values.

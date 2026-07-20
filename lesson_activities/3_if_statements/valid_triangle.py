# A triangle can be formed from 3 sides if all pairs of 2 sides are longer than the third side.

#=======================
# TODO
# Define a function 'isValidTriangle' that takes 3 arguments.  (For example 'a', 'b', 'c')
# The arguments correspond to the side lengths of a triangle.
# return True if the sides can form a triangle, return False if they can't



#=======================
# Tests are provided for you:
def main():
    assert isValidTriangle(3,4,5), "isValidTriangle failed test with a = 3, b = 4, c = 5"
    assert isValidTriangle(1,1,1), "isValidTriangle failed test with a = 1, b = 1, c = 1"
    assert isValidTriangle(2,4,9) == False, "isValidTriangle failed test with a = 2, b = 4, c = 9"
    assert isValidTriangle(9,4,2) == False, "isValidTriangle failed test with a = 9, b = 4, c = 2"
    assert isValidTriangle(4,9,2) == False, "isValidTriangle failed test with a = 4, b = 9, c = 2"
    assert isValidTriangle(2,3,5) == False, "isValidTriangle failed test with a = 2, b = 3, c = 5"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()
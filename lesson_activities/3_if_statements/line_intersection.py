#=======================
# TODO
# Find the intersection point of the two lines
# y = a1 * x + b1
# y = a2 * x + b2
# Calculate and assign the coordinates of the intersection point to the variables x and y, then return (x,y)
# If this is not possible because the lines do not intersect, return (0,0)
def findIntersectionPoint(a1,b1,a2,b2):
    x = 0
    y = 0
    return (x,y)



#=======================
# Tests are provided for you
def main():
    assert findIntersectionPoint(1,0,-1,0) == (0,0), "findIntersectionPoint failed test"
    assert findIntersectionPoint(1,0,2,-6) == (6,6), "findIntersectionPoint failed test"
    assert findIntersectionPoint(-1,10,4,1) == (1.8,8.2), "findIntersectionPoint failed test"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()
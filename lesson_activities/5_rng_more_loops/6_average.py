#=======================
# TODO
# Calculate the average value in 'list_in'
# The average is the sum of all the elements in the list divided by the number of elements.
# Use a while-loop to calculate the sum, then calculate and return the average.
# Afterwards, we will cover how to solve the same problem with a for-loop.
def average(list_in):
    sum = 0
    i = 0
    
    return 0



def main():
    assert average([0]) == 0, "average failed test with list_in = [0]"
    assert average([1,1,1]) == 1, "average failed test with list_in = [1,1,1]"
    assert average([-4,0,4]) == 0, "average failed test with list_in = [-4,0,4]"
    assert average([100,200]) == 150, "average failed test with list_in = [100,200]"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()
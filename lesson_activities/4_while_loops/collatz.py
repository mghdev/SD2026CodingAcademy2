# The Collatz Process goes like this:
#    if you have an even number, divide by 2
#    otherwise, multiply by 3 and add 1


#=======================
# TODO
# Define a function named 'collatz' with 1 parameter 'n'
# It should return the number of steps of the Collatz process that it takes to reach 1 starting from n
#
# Pseudocode describing what the function should contain:
#
# Start with a counter at 0 and your number n
# While your number is not 1
#    perform a Collatz Process step on your number
#    add 1 to the counter
# Return the value of the counter

    


#=======================
# Tests are provided for you.
def main():
    assert collatz(1) == 0, "collatz failed test with n = 1"
    assert collatz(3) == 7, "collatz failed test with n = 3"
    assert collatz(7) == 16, "collatz failed test with n = 7"
    assert collatz(14) == 17, "collatz failed test with n = 14"
    assert collatz(30) == 18, "collatz failed test with n = 30"
    assert collatz(8) == 3, "collatz failed test with n = 8"
    assert collatz(71) == 102, "collatz failed test with n = 71"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()
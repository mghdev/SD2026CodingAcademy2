# The Fibonacci sequence goes 1 1 2 3 5 8 13 21 34 55 89 ...
# Each element in the sequence is the sum of the previous two.
# The rules are:
#   fibonacci(0) is 1
#   fibonacci(1) is 1
#   fibonacci(n) is fibonacci(n-1) + fibonacci(n-2)


#=======================
# TODO
# Calculate the nth number in the Fibonacci sequence
# Return only the nth number in the sequence, not the entire sequence up to that point.
def fibonacci(n):
    return 0


#=======================
# TODO
# Call fibonacci() with some specific values to test it
# For example:
#   fibonacci(0) should return 1
#   fibonacci(2) should return 2
#   fibonacci(20) should return 10946
#   fibonacci(40) should return 165580141
def main():
    print(fibonacci(40))



if __name__ == "__main__":
    main()
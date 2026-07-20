# To quote wikipedia:
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400. 
# For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.

#=======================
# TODO
# Define a function named 'isLeapYear' with 1 parameter 'year'
# It should expect int year numbers as arguments and return True if the year is a leap year, false otherwise.
# For example, the call 'isLeapYear(2000)' should return 'True'.
# Use the modulo operator '%' to determine whether the year is divisible by 4, 100, and/or 400
# Use if-statements to return the right value under the right combination of conditions



#=======================
# Tests are provided for you
def main():
    assert isLeapYear(1) == False, "isLeapYear failed test"
    assert isLeapYear(4), "isLeapYear failed test"
    assert isLeapYear(444), "isLeapYear failed test"
    assert isLeapYear(1700) == False, "isLeapYear failed test"
    assert isLeapYear(1600), "isLeapYear failed test"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()
# Data Design Exercise
#=======================
# TODO
# If you haven't already, read the preceding data discussion for context.
# As a class, we will agree on a particular data model to use for payroll records.
#
# Holy Roman Foods Inc employs a baker named Charles Martel who is paid $27.50 per hour.
# Charles worked from 3:30 in the morning to 9:00 in the morning on Monday the 2nd of March, 2026.
# Create one or more variables and assign to them a representation of Mr Martel's employment and this work period.
# Create a variable named 'monday_pay' and assign an expression that uses your record of Charles's work to calculate how much money he earned that day.



#=======================


print("")
target = 27.5 * 5.5
margin = 0.005
if not (target-margin <= monday_pay <= target+margin):
    print("Incorrect pay result.")
    exit()

print("Success.\n")

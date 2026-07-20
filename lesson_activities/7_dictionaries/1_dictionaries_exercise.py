# Dictionaries Exercise
#=======================
# TODO
# Here is a dictionary mapping some people's names to their phone numbers.
# Paul recently changed his number to "386 682 3342" and Duncan changed his to "386 474 4652".
# Update the dictionary to reflect these changes.

phone_numbers = {
    "Paul" : "253 287 3433",
    "Duncan" : "253 123 2770",
    "Stilgar" : "386 497 3626"
}

if not phone_numbers["Paul"] == "386 682 3342":
    print("Paul's phone number is not correct.")
    exit()

if not phone_numbers["Duncan"] == "386 474 4652":
    print("Duncan's phone number is not correct.")
    exit()

print("Success")
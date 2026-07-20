# Dictionaries Exercise
#=======================
# TODO
# Create a variable named 'read_me' and assign a literal dictionary with the following characteristics:
#   3 key-value pairs
#   all keys are str
#   all values are lists containing 2 elements

read_me = {
    
}

if not type(read_me) == dict and len(read_me) == 3:
    print("Your variable is not a dictionary with 3 key-value pairs.")
    exit()
    
for k in read_me:
    if not type(k) == str:
        print("At least one of your keys is not a str")
        exit()

for v in read_me.values():
    if not type(v) == list and len(v) == 2:
        print("At least one of your values is not a list of length 2.")
        exit()

print("Success")
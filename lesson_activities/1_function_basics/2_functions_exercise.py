# Funtions Exercise
#=======================
# TODO
# Below is a partial definition of the function 'fourSeasons'.
# It should return a list object containing the names of the seasons as str:  "Summer", "Autumn", "Winter", and "Spring".
# To accomplish that, create a variable 'seasons' in the function body before the provided return statement.
# Assign a list literal containing the correct str values to 'seasons'. Order is not important.
# After the function definition, call fourSeasons and print the return value.
# Always run your code!

def fourSeasons():
    
    return seasons

#=======================


result = fourSeasons()
if not (type(result) == type(list())):
    print("Return value has the wrong type.")
    exit()

def checkForSeason(answer,season):
    if not (season in answer):
        print("\nMissing '",season,"'.\n",sep="")
        exit()

print()
checkForSeason(result,"Summer")
checkForSeason(result,"Autumn")
checkForSeason(result,"Winter")
checkForSeason(result,"Spring")
print("\nSuccess.\n")
# Variables Exercise
#=======================
# TODO
# The average distance from the Sun to the Earth is roughly 149 597 871 km. This distance is called the 'Astonomical Unit' (au)
# Here are approximate distances from the Sun to the orbits of all the planets, in au:
# Mercury:  0.39  au
# Venus:    0.72  au
# Earth:    1.00  au
# Mars:     1.52  au
# Jupiter:  5.20  au
# Saturn:   9.58  au
# Uranus:   19.22 au
# Neptune:  30.05 au
# 
# Create variables named after some of the planets of our solar system:
# 'mercury_km', 'venus_km', 'earth_km', 'mars_km'
#
# Assign the literal int 149597871 to 'earth_km'.
# Assign the correct distance in km from the Sun to the other planets using expressions based on your 'earth_km' variable.
# Your results should be in whole km only, discarding fractions.  ('int' type!)



#=======================

print("")
if not (type(mercury_km) == type(venus_km) and type(venus_km) == type(earth_km) and type(earth_km) == type(mars_km) and type(earth_km) == type(int())):
    print("Variable types are incorrect.\n")
    exit()

if not (mercury_km == 58343169 and venus_km == 107710467 and earth_km == 149597871 and mars_km == 227388763):
    print("Values stored in variables are incorrect.\n")
    exit()

print("Success.")
print("Mercury:",mercury_km,"km")
print("Venus:",venus_km,"km")
print("Earth:",earth_km,"km")
print("Mars:",mars_km,"km")
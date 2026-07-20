# Animal Populations Background

Biologists and ecologists who study animals want to know how large wild populations are.
It's usually not possible to count every single individual, so scientists resort to a number of other techniques.

One process works something like this:
 - Identify the limits of the area to investigate.
 - Do a pass through the area. Capture and mark animals you see of the type you are trying to count, then release them.
 - Wait some time (e.g. a few months or a year) to allow the marked animals to move around and get mixed up with the rest of the population.
 - Do a second pass; capture every target animal you see and count how many are marked (recaptured) vs un-marked.

At the end, we can estimate the total population n as:
> n = c * m / r

Where c is how many animals were counted in total on the second pass, m is the total marked animals in the area, and r is how many marked animals were recaptured.

For example, if we recapture 14 out of 20 total marked individuals, then we would estimate that we found that same fraction of the total population. If we counted 84 animals in all, then our total population estimate would be:
> n = 84 * 20 / 14

# Scenario

Imagine you are part of a team studying the population of moose in a 50km x 50km region of forest in Finland. Your (very brave) teammates captured a bunch of moose, marked them with GPS locators, and recorded physical characteristics like sex, weight, height, and body length.

1) What Python data type would you use to represent the weight of a moose? How about height and length?

2) Which type would you use to represent the sex of a moose? What value would correspond to male? How about female?

3) If you wanted to have a single object representing a moose individual, which type would you use? What value could correspond to a female moose that weighs 403 kg, is 2.1m tall, and 2.4m long?

4) GPS coordinates are a pair of angles called latitude and longitude. How would you represent the GPS position of a moose?

Due to limited time, the team decides to divide the forest into a grid of 10km x 10km square areas and do their second counting pass in only some of these areas. Another member of the team has written a script to convert global GPS positions to an orthonormal xy-coordinate system with its origin at one corner of the 50x50km forest. Coordinates are floats in km, ranging from 0.0 to 50.0 in each direction.

5) You need some way to identify which grid square each moose is in. How would you label the squares?

6) Your team wants a function that goes through the position data, figures out how many moose are in each grid square, and collects the results into a single object. Describe the type and possible contents of such an object.
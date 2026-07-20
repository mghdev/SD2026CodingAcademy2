# Data Design

One of the most important parts of designing a program is to decide what data it needs and how to organize it.
For this discussion, read the following prompt about a software project and think about what types of objects and variables you would need to create if you were writing code for that project.

Some of this may be difficult using only the types you have experience with; that's ok! There are always many different ways to approach design questions like this. With a little creativity, it's possible to model very complicated systems with very simple data types. Ultimately, everything in a computer is a bunch of bits.

# Holy Roman Foods

You are working on accounting software that keeps track of sales and expenses at Holy Roman Foods Inc (a grocery store).
Among other things, this software tracks the store's weekly payroll: it needs to know which employees worked for how many hours on which days at what pay rate.

1) Which basic Python type would you use to represent an employee's hourly pay rate?

2) How would you represent an employee's name? Think about the data type and how many objects you might need.

3) How would you represent dates? What value would be stored in a variable to represent the 4th of July, 2026? Should you also store which day of the week that is?

4) Every day, the store records what time each employee starts work and what time they finish, to the nearest 15-minute interval. What data type would you use to represent these timestamps? What value would be stored in a variable to represent 8:45 in the morning?

(Bonus) Do the date and time need to be separate objects? Why or why not? (Think about this AFTER the rest of the questions)

5) A worker named Frederick Barbarossa is paid $23.70 per hour. Your software needs to have a record of this fact; in other words, we need a single object that associates Mr Barbarossa with his regular pay rate. What type should this object be? What value would you assign to a variable to represent Frederick's employment?

6) Frederick worked from 8:00 in the morning to 1:00 in the afternoon (13:00) on Friday January 23rd, 2026. How would you represent this in a variable? You need a single object that can be used to identify which employee was working and when.

By some cosmic coincidence, Holy Roman Foods Inc has a second employee whose name is ALSO Frederick Barbarossa. This second Frederick works as a butcher and is paid $27.50 per hour. Does this change your answer to the two previous questions?

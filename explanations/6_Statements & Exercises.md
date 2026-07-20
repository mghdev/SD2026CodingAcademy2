> [!NOTE]
> While going through this document, create a test script to type out code examples that show you something new, so you can run them for yourself.

# Statements

A 'simple statement' is a single line of code that *does* something.
We've already seen one example of a statement: assignment. Assignment is a line of code that stores an object in a variable.

```python
even_number = 2
meme_text = "I have the high ground."
```

The following are some more examples of simple statements that will come up during this course. This is just a quick overview.

## pass

The pass statement does... nothing. This is called a 'no-op' or 'null operation'. Its purpose is to fill a line of code when you need one for syntax reasons but aren't ready to write your real code yet. If leaving a line blank temporarily would cause errors while you're working on a different part of your code, you can fill the line with a pass.

```python
pass
```

Many files in this repository have pass statements in places that are meant to be replaced by your code.

## return

The return statement can only be placed inside function definitions. The expression after a return is what the function will evaluate to when called -- this is the 'return value'.

```python
def alwaysEvaluatesToThree():
	return 3

print(alwaysEvaluatesToThree())
```

Many exercises in this course will ask you to write functions that return something specific. For example:
```python
# The function 'add' has two parameters.
# It should return the sum of its arguments.
# Complete the body of the function so that it returns the correct value.
def add(a,b):
	pass
```

Notice the placeholder 'pass' statement. A function definition with no code in it is an error!
A correct solution would be:
```python
def add(a,b):
	return a+b
```

And you might check your work by calling the function and printing the return value, for example:
```python
print(add(4,9))
print(add(-2,2))
```

All together:
```python
# The function 'add' has two parameters.
# It should return the sum of its arguments.
# Complete the body of the function so that it returns the correct value.
def add(a,b):
	return a+b

print(add(4,9))
print(add(-2,2))
```


## import

The import statement is for loading code from another module (which just means a file) into the current module. For example, the 'math' module contains the value of pi and some trigonometric functions:

```python
import math
print(math.pi)
print(math.sin(-5.5 * math.pi))
```

A list of all the modules that come with python by default (The Python Standard Library) can be found at:
https://docs.python.org/3/library/index.html
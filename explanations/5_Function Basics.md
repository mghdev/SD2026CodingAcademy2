> [!NOTE]
> While going through this document, create a test script to type out code examples that show you something new, so you can run them for yourself.

# What is a Function?

A function is a block of code that is defined once and then executed (or 'called') later, potentially many times.

# Defining Functions

A function definition includes a name, a list of parameters, and a body of code. The syntax looks like this:

```python
def name(parameters):
	body
```

To start, here are some examples with no parameters:

```python
def firstFunction():
	print()
	print("Goooooood morning, Los Angeles!")
	print("Coming to you live from inside a function.")

def secondFunction():
	print("We've got a great show lined up for you today.")

def thirdFunction():
	pass
```

>Notice in this example that all of the code in function bodies is indented to the right. This is *required*, and there are other features of Python that also require indentation. To indent a line of code, insert either a tab or 4 spaces at the beginning of the line. Different numbers of spaces are possible, but you *must* be consistent. You cannot mix tabs and spaces, and you cannot mix different amounts of spaces.

As we covered previously, after a function is defined you call it by typing its name and a pair of parentheses:

```python
firstFunction()
secondFunction()
thirdFunction()
firstFunction()
```

The code in a function's body is not executed when the function is defined. Instead, that code runs each time the function is called. When Python encounters a function call, you can imagine that its instruction pointer jumps to the first line of code in that function's body. Once the last line of code in the function body has been executed, Python's instruction pointer returns to the line of the function call.

# Return Value

A function call is an expression that evaluates to an object called the function's 'return value'. By default, functions return 'None'. To produce any other value, a function needs to explicitly return an expression using a 'return' statement:

```python
def alwaysEvaluatesTo3():
	return 1+2


print("First calll: ",alwaysEvaluatesTo3())

what_number_could_it_possibly_be = alwaysEvaluatesTo3()
print("Second call: ",what_number_could_it_possibly_be)
```

When a return statement is executed, Python evaluates the expression after the 'return' and then the program counter is immediately reset back to the line that the function was called from. The return value of the function becomes the result of the function call expression. Any code in a function body after a return will not be executed:

```python
def lotsOfUnusedCode():
	print("We're calling a function!")
	return "Hark, a str."
	print("These prints will never execute.")
	print("After a return, the program counter goes back to the caller.")

value = lotsOfUnusedCode()
print("The return value was: ",value)
```

On its own, the ability to return a value might not seem that useful. However, functions can also accept inputs and base their return value on those inputs.

# Parameters and Arguments

When defining a function, its inputs are called 'parameters'. 

Parameters are variables that get re-created each time a function is called and assigned values that are passed in from the caller. They are declared between the parentheses in a function definition, separated by commas.

The actual values passed in as inputs when calling a function are called 'arguments'.

```python

def learningAboutParameters(parameter0, parameter1, another_parameter):
	print("First argument: ",parameter0)
	print("Second argument: ",parameter1)
	print("Third argument: ", another_parameter)

print("First call:")
learningAboutParameters(2,"Argon",-3.14)

print("Second call:")
first_argument = 6
second_argument = 9
third_argument = 12
learningAboutParameters(first_argument,second_argument,third_argument)

print("Third call:")
x = 4
learningAboutParameters(x**2,x/2,x-1)
```

It is common for a function's parameters to be involved when creating its return value. As a toy example, if we want a function that adds two numbers together:

```python
def add(first_number,second_number):
	return first_number + second_number

print("2 + 8 is ",add(2,8))
print("5 - 1 is ",add(5,-1))
```
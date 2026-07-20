> [!NOTE]
> While going through this document, create a test script to type out code examples that show you something new, so you can run them for yourself.

# The print Function

To make a Python script output text to your console, call the built-in print function.

```python
print("Hello World!")
```

print() can take multiple arguments.

```python
some_text = "lorem ipsum"
print("First Argument",some_text,"Third Argument")
```

print() can handle many different types, as long as they can be converted to str.

```python
number = 27.0
print(30,"white horses on a red hill.",number,[0,3,6])
```

You can print multiple lines of text at once in several different ways. For example:

```python
print("The special newline character...\nA backslash and the letter n.\n")
print("""
Multi-line string literals
are written with three pairs
of quotation marks.""")
```

print() has several default behaviors that you can modify using a feature called 'named arguments'.
print() separates the printing of each regular argument with a single blank space. You can specify a different separator string by assigning a different value to the named 'sep' argument, like this:

```python
print("With no sep:")
print(2,3,5,7,11)
print("With a custom sep:")
print(2,3,5,7,11,sep="+")
```

print() ends each call by going to the next line (e.g. by printing a newline character '\n).
You can specify different end text using the 'end' named argument. Typically you would do this to set 'end' to an empty string, causing subsequent prints to start on the same line, like this:
```python
print("The first print",end="")
print(" and the second print will output to the same line.")
```


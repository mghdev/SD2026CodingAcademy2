> [!NOTE]
> While going through this document, have a Python shell open so that you can run code examples for yourself.

# Function Calls

Another common use for identifiers is to name 'functions'.
A function is a block of previously-defined code that you can execute using its name.

To 'call' a function, you type the name of the function followed by a set of parentheses ().
Each of the data types we have covered so far comes with a function for constructing objects of that type:

```python
int_variable = int()
float_variable = float()
str_variable = str()
list_variable = list()
bool_variable = bool()
```

> What values are stored in the variables from this example?

A function call is an expression. The object that it evaluates to is called the 'return value' of the function.

Most functions accept inputs, called arguments, that they can use to produce their return value. The arguments go inside the parentheses when calling the function.
For example, those built-in type constructor functions can be used to convert values to a different type:
```python
float_version = float(42)
number_text = "28"
actual_number_var = int(number_text)
back_to_str = str(actual_number_var)
```

>Can you come up with arguments to pass to the int() function that cause errors?

Exactly how many and what kinds of arguments a function will accept is specific to that function and depends on how it was defined.
Here are some more examples of built-in functions for you to call:

```python
len("drachma")
exit()
max(1,5)
min(-1,6,2,-3)
bin(12)
type(5)
abs(-9)
```

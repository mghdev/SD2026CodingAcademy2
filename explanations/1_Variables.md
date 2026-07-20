
> [!NOTE]
> While going through this document, have a Python shell open so that you can run code examples for yourself.

## Identifiers

An identifier is a name defined by a programmer to refer to some object.
> Identifiers can contain upper- and lower-case letters, digits, and underscores.
> A-Z, a-z, 0-9, \_
> Identifiers **must** start with a letter or underscore, not a digit.

These are valid identifiers:
```python
a
var1
DOOM
_local
o_0_s_I_l_L_y_0_o
```

These are **not** valid identifiers:
```python
2a
5nine_r27
```

## Variables

One common use of identifiers is to name variables.
A variable is a container for data. It holds an object that can be re-used and potentially modified while a program is running. Variables are created with the assignment operator '='

```python
a = 5
var1 = "this is a str"
DOOM = 40 + 2
```

The lefthand side of an assignment operation is an identifier, and the righthand side is an expression. The identifier on the left becomes the name of a variable, and the value of the expression on the right is stored in that variable.

Assignment can be used to replace the value stored in an existing variable:
```python
prime_number = 7
prime_number = 23
prime_number = 2
```

After these 3 lines of code are executed, there is only a single variable 'prime_number' with the value 2.

Once a variable has been created, its name becomes a valid expression that evaluates to the object stored in it:
```python
my_var = 23   # creates a variable named 'my_var'
2 * my_var    # 'my_var' evaluates to the int '23'
my_var - 16
other_number = my_var + 1
```

> What value is stored in 'other_number'?

Note that assignment is not an expression. It does not evaluate to an object. This code raises a SyntaxError:
```python
(a = 3) + 2
```

## Keywords

There is a short list of identifiers which are reserved by Python and may not be re-defined:
https://docs.python.org/3/reference/lexical_analysis.html#keywords
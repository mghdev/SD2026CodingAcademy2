# Boolean Expressions

Boolean expressions evaluate to 'bool'-type objects. They are often the result of comparison operations or combinations of smaller boolean expressions, and are often used as conditions that control whether certain blocks of code will execute or not.
The literal bools are
```python
True
False
```

You can generate a bool value using relational operators:  ==, >, <, >=, <=
```python
3 == 3.0
27 - 5 < 24
"orbital" >= "yak"
"A" < "a"
[0,2,4,8] <= [0,2,6]
```

These operators compare the values of 2 expressions. 
>Not all objects can be compared to one another! Can you cause a TypeError with a relational operator?

You will often want to modify and combine boolean expressions into a single larger condition. This can be done with the boolean operators: not, and, or

```python
True and False
(-9 < 0) or (4 == 4.1)
not True
(len("barbarian") > 5) and not (5*5 == 25)
```

# If Statements

If statements are a compound statement, or a pattern of code accross multiple lines that has some effect. In particular, if-statements are made up of a condition and a body of code, like this:
```python
if condition:
    body
```

Like with function definitions, the body *must* be indented one level relative to the 'if'.

The condition is an expression that will be interpreted as a bool. When the condition is True (or True-like) the body of the if statement will execute. When the condition is false, the body will be skipped and execution jumps to the next line of code after the body.

```python
a = 22
if a > 20:
    print("The variable was greater than 20.")
    print("... I can have multiple lines of code in the body of a single if-statement.\n")
```

The condition can contain any boolean expression, no matter how complicated:
```python
x1 = 50
if ((True or 1-1<0) and (((2+2)%3==0) and True) or x1 == 100/2) :
    print("That crazy thing was True.\n")
```


Since the body is allowed to contain statements, if-statements can be nested.
Nested if-statements result in multiple levels of indentation:

```python
a = 25*2
b = 625**0.5
if not a == b:
    print("a and b were different:",a,b)
    a = a/4
    if a == b:
        print("a was divided by 4, and now a and b are equal:",a,b)
        b = 40
b = 3
print("Now b is 3 no matter what happened before:",b)
print("")
```

You can also create a block of code to be executed if the condition evaluates to False using an 'else' clause:

```python
x = 90-max(50,100)
if x > 0:
    x = 0
    print("Positive changed to zero.\n")
else:
    print("x is not positive.\n")
```

Or, you can chain multiple ifs and elses together with 'elif' (short for else if)

```python
x = 90-max(50,100)
if x > 0:
    x = 0
    print("Positive changed to zero:",x,"\n")
elif x < 0:
    x = -x
    print("Negative changed to positive:",x,"\n")
else:
    print("x was zero:",x,"\n")
```

In the context of if-statement condition expressions, there are some funny rules about what is considered true and false.

False, None, any type of numeric value equal to 0, and empty containers like the empty str "" or empty list [] are all considered false.

*Everything else* is considered true.

```python
if 27:
    print("1) Yes.")
else:
    print("1) No.")

if []:
    print("2) Yes.")
else:
    print("2) No.")

if len("abc")-3:
    print("3) Yes.")
else:
    print("3) No.")
```

> [!NOTE]
> While going through this document, have a Python shell open so that you can run code examples for yourself.

# Expressions

An expression is a piece of code that evaluates to some object. When code is being executed, this means expressions get processed to produce a single value, like a number, some text, a list, or a truth value.

## Literal Values

The most straightforward kind of expression is just a 'literal', like these:

```python
23
0
5.7

"capybara"
'single-quoted string'
"double-quoted string"

"""multi-
line
string
(three pairs of matching quotes)"""

[0, 4.6, -1]
["list","of","strings"]
[22, [0,1], 8]

True
False

None
```

A literal does not describe any actions or computations, it directly represents an object with a particular type and value.

The 'value' of an object corresponds to a particular pattern of bits. However, when talking about values, we use regular human representations and not strings of binary digits. You can refer to a literal expression as a value e.g. the value "Water" instead of "01010111 01100001 01110100 01100101 01110010".

## Data Types


The 'type' of an object is information relating to how the value should be interpreted by code acting on it or by humans who read it.

Here are the types that the example literal expressions above evaluate to:
>'int' (short for 'integer') is the type representing whole numbers	 
>
>'float' (short for 'floating point number') is the type representing numbers with a decimal point 
>
>'str' (short for 'string') is a specialized sequence for text characters  
>
>'list' is a sequence that can hold objects of any type
>
>'bool' is the truth-value type. It has only 2 possible values, 'True' or 'False'
>
>'NoneType' is a special type with only a single value 'None'. It represents the absence of a value.

The same exact pattern of bits may mean different things depending on the type of the object it's part of. As an int "01100001" is 97, but in a str it's the character "a".

An object's type also says something about its size and how it's organized in a computer's memory. For example, a 'float' is 64 bits.

## Arithmetic Operators

Expressions can be modified or combined into larger expression with 'operators'. Operators perform an action to produce a value based on other objects.
Python's arithmetic operators are: +, -, \*, /, \*\*, //, %

Here are a bunch of expressions using arithmetic operators and literals:

```python
2+5
5+2
-7
3.0-1
2+5*3-1
"a"+"b"
5*2.2
15.9/3
2**3
3**2
10%3
7//2
"c"*5
```

>Try writing some expressions of your own using these operators!
>
>Which operators work with which combinations of types? 
>What do they do?
>What type is the result?
>What kinds of errors can you cause?

## Parentheses

Python arithmetic follows all the typical rules for order of operations.
You can use parentheses to group expressions and control the order of operations. Inner parentheses are evaluated first.
```python
(2+5)*(3-1)
-(1+1)
((5+1)-(3-2))/(1+1)+2
```


## More Operators

There are other kinds of operators which you will use in future lessons.

Relational operators: \==, >, <, >=, <= (for comparing things)

```python
4 == 7
4 < 7
2.0 >= 2
"bee" > "bed"
```

Boolean operators: not, and, or
```python
not True
(3+2 > 4) and (-12 < 0)
False or 22%2 == 0
```


The subscript operator: [] (for pulling elements out of a sequence)
```python
"alphabet"[0]     # evaluates to "a"
"alphabet"[1]     # evaluates to "l"
"alphabet"[2]     # evaluates to "p"
"alphabet"[3]     # evaluates to "h"
"alphabet"[4]     # evaluates to "a"


[2,4,8,16,32][2] # evaluates to 8
```
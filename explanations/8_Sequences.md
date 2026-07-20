# Sequences

A sequence is a numbered ('indexed') collection of objects. The first object in a sequence has index 0, and each subsequent object has +1 index.

This course will mainly cover the sequence types 'list' and 'str'

## list

A list is a sequence of objects of any type. Literal lists are written as comma-separated expressions between square brackets []

```python
int_list = [0,1,2,3,4]
float_list = [2.3, 4.1, 6.9, 10.2]
str_list = ["a","Mark","wow"]
list_list = [[2,1],["q","s"]]
mixed_list = [-4.5,"str",[0],42]
```

You can access items in a list by index using the subscript operator, which is also a pair of square brackets []
A list value followed by square brackets with an index inside evaluates to one element from the list, like so:
```python
int_list[4]   # 4
float_list[0] # 2.3
str_list[1]   # "Mark"
list_list[1]  # ["q","s"]
i = 0
mixed_list[i]
```
The index passed into the subscript operator MUST be an int. It cannot be a float, even if the float is equal to some integer.

Negative indices in the subscript operator count backwards from the end, with index -1 being the final element
```python
int_list[-2]    # 3
float_list[-1]  # 10.2
mixed_list[-3]  # "str"
```

The len() function can take a list as an argument and returns the number of elements in the list
```python
len(int_list)   # 5
len(list_list)  # 2
```

Lists can be concatenated with the '+' operator. This means combining end-to-end into a single new list.
```python
list_a = [1,3]
list_b = [2,4]
list_a + list_b     # [1,3,2,4]
list_a + int_list   # [1,3,0,1,2,3,4]
```

Lists can be repeated with the '*' operator. This means making a new list with the elements of the original repeated some number of times.
```python
list_a*3    # [1,3,1,3,1,3]
[0]*5       # [0,0,0,0,0]
```

You can check whether a specific value is an element of a list with the 'in' operator. This creates a boolean expression.
```python
int_list = [0,1,2,3,4]
list_list = [[2,1],["q","s"]]

3 in int_list   # True
7 in int_list   # False
2 in [1,2,3]    # True
[2,1] in list_list  #True
```

## Slices

Finally, you can extract multiple elements from a list at once using a 'slice' in the subscript operator.
A slice is two or three ints separated by colons ':'
sequence[start:stop]
sequence[start:stop:step]
The version with only start and stop is the same as [start:stop:1]

```python
int_list[0:2]   # [0,1]
float_list[2:3] # [6.9]
int_list[0:5:2] # [0,2,4]
int_list[0:4:2] # [0,2]
```

Taking a slice always evaluates to another list, even if the slice contains only one element.

The slice includes all the elements starting from the 'start' index, stopping at (and NOT including) the 'stop' index.

It jumps forward by 'step' indices between each element that gets included. Setting the 'step' to 2 skips over every 2nd element, for example.

You can leave the start and stop in a slice blank. When you do, the slice will start at the beginning of the sequence or stop after it passes the last element.
```python
int_list[:3]    # the same as int_list[0:3]
int_list[2:]    # [2,3,4]
int_list[:]     # the entire list [0,1,2,3,4]
int_list[::-1]  # the entire list... but stepping backwards [4,3,2,1,0]
int_list[::-2]  # What do you think this evaluates to?
```

## str

All of the operators described above can be used with str objects as well, and they work exactly the same way.
Literal str are sequences of characters between pairs of quotation marks:
```python
str1 = 'abcdefg'  # single quotes can be used
str2 = "foo and bar" # double quotes can be used
str3 = """Triple quotes
let a literal str
span multiple lines"""

str1[0]         # subscript with an index works fine
str1[:3]        # subscript with a slice
"2"+"argh"      # concatenate
"free "*2       # repeat
"f" in "free"   # check membership
```

## Mutability

There is one basic operation that can be performed with list that is not possible with str.
You can replace individual values in a list variable using assignment.
```python
numbers = [7,22,11,34,17]
numbers[0] = -1
numbers[4] = -1
```

>Try it out in interactive mode. Try it with a str as well.

This feature is called mutability (ability to change). list is a 'mutable' sequence type, str is 'immutable'.

The other sequences that may come up in this course, 'tuple' and 'range' are both immutable.
We will also cover one other container type, the 'dict' (dictionary), which is mutable.
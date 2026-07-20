
# dict

'dict' (short for 'dictionary') is a type of collection object, like a list or a str. The difference is that dict is not a sequence, its elements are not indexed from 0 to len()-1. Instead, a dict contains key-value pairs, where the key takes the role of an index and the value is what gets returned when you look up a key.

It may help to think of a real-life dictionary; keys are the words you look up, values are like the definitions.

## Literals
A literal dict can be written with curly braces {} containing key:value pairs separated by commas, like this:
```python
dict_0 = {"a":4,"g":89,"c":21}
```
The keys in dict_0 are "a", "g", and "c"

The values are 4, 89, and 21

## Accessing

We can access the value associated with a key using the subscript operator, just like indices in a sequence:
```python
print(dict_0["a"])
print(dict_0["g"])
print(dict_0["c"])
```

## Modifying

You can add a new entry to a dict by assigning a value to a key that does not exist yet:
```python
dict_0["z"] = 11
print(dict_0)
```

You can update the value associated with an existing key in the same way:
```python
dict_0["a"] = -6
print(dict_0)
```

## Iterating
You obtain an iterable view of the keys or the values on their own using the keys() and values() methods.
```python
for key in dict_0.keys():
    print(key)

for value in dict_0.values():
    print(value)
```

Creating a list from a dictionary also gives you just the keys, e.g.
```python
print( list(dict_0) == list(dict_0.keys()) )   #True
```
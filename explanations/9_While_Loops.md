# While Loop

The 'while' loop is the first statement we will look at that allows the same code to repeat multiple times
Its syntax is almost identical to the if-statement:
```python
while condition:
    body
```

The difference between if-statements and while-loops is that when control reaches the end of a while loop's body, it returns to the condition and evaluates it again.

If the condition continues to be true, the body gets executed again (then it returns to the condition again, etc...)

If the condition has become false, while behaves just like an if: the body is skipped and program execution continues from the next line after the end of the loop.

Copy this loop into a script of your own and try it out.
```python
i = 0           # this line is the loop's 'initialization'
while i<5:      # the loop's condition
    print(i)
    i += 1      # the loop's 'increment'
```

The condition in a loop often involves a variable whose only purpose is to control when the loop stops, the 'loop variable'

Before the beginning of the loop, the loop variable is created and initialized. Often this initial value will allow the loop's body to run at least once.

Somewhere inside the loop's body, there should be some code that modifies the loop variable (or at least potentially can), often called the 'increment'

Putting it all together, we have 4 parts to a typical loop:
the initialization, the condition, the body, and the increment (which might be part of the body)

```python
initialization
while condition:
    body
    increment
```

## Examples

```python
print("Counting down...")
i = 10
while i>0:
    print(i)
    i = i-1
print("Liftoff!")
```

```python
print("Powers of 2 up to 2^10:")
stopping_point = 2**11
n = 1
while n < stopping_point:
    print(n)
    n = n*2
```

```python
# You can nest loops just like if-statements
i = 0 
while i<5:
    # the body of the outer loop is the entire inner loop.
    j = 0
    while j<4:
        print(i,j," Sum:",i+j)
        j += 1
    # the outer loop's increment comes after the inner loop
    i += 1
```

## Looping Over Sequences

Loops are commonly used to do something with each individual element of a sequence.

In Python, this is always done with a 'for'-loop rather than a while-loop. We will learn about for-loops later, but just to show another example, here is what that looks like with a while-loop:
```python
my_list = [5,16,8,4,2,1]
i = 0
while i < len(my_list):
    element = my_list[i]
    if element % 2 == 0:
        print(element)   #print only the even elements
    i += 1
```

while-loops are for situations when you don't know in advance how many times the loop needs to run.

For example, if you want to allow a user to choose when the loop exits:
```python
word = input("Gimme a word: ")
while not (word[0] == "A" or word[0] == "a"):  #keep going until the input word starts with 'a' or 'A'
    word = input("Gimme a word: ")
```
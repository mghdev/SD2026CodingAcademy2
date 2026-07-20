Here is a very simplified model of (some of) what your computer does to run a Python script.

## Program Counter

There is a number stored in your computer's processor called a 'program counter' or 'instruction pointer' that tracks which instruction the processor should execute next. On modern hardware the situation is actually more complicated, but you can imagine that a little piece of the processor tells the rest of it where to look in the computer's memory to find its next instruction.

## Instruction Cycle

Your processor fetches the instruction that the program counter is pointing to, then advances the program counter and executes the instruction. Then the whole process repeats.

## What is a Program?

In this model, a program is just a sequence of instructions stored in a computer's memory.

## Running a Python Script

For the purposes of this course, think of the program counter as pointing to a particular line of your Python code. Python reads that line, then executes it and moves the counter to the next line of code. It repeats this process until an error or exit(). Depending on exactly what your code says, the 'next line of code' might literally be the subsequent line of text in your code file, or it might be 100 lines farther down, 20 lines back, or in a different file entirely.
# Warmup

As a warmup, use your Python shell to see what the following expressions evaluate to:

```python
2%3
3%3
4%3
5%3
6%3
7%3
8%3
9%3
```

What pattern do you see?

How about these expressions:
```python
2//3
3//3
4//3
5//3
6//3
7//3
8//3
9//3
```

# Grid Coordinates

There are several coordinate systems or ways of labeling squares in a grid that are useful for different purposes. It often makes sense to convert a position back and forth between these systems as need for particular representations arises.

Let's consider three different systems:

1) Fine-grained (or continuous) position data. In 2 dimensions, this would be pairs of coordinates along axes aligned to the grid, with the origin at a corner.

2) Row and column numbers, or coarse-grained coordinates. Starting from the origin, this would tell you how many grid squares to move horizontally and vertically to reach a particular cell; this system does not distinguish between different positions within a square. Here is the layout of example (row,column) numbers for a 5x4 grid with the origin in the top-left, x-axis to the right and y-axis down.

(0,0) (0,1) (0,2) (0,3) (0,4)

(1,0) (1,1) (1,2) (1,3) (1,4)

(2,0) (2,1) (2,2) (2,3) (2,4)

(3,0) (3,1) (3,2) (3,3) (3,4)

3) Indices. This means simply numbering each cell in the grid. If there are 16 cells in a 4x4 grid, for example, you might number them 0 thru 15. Notice that a cell's number corresponds conveniently to an index in a list.
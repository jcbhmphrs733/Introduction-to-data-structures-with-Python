# Intro to Trees
Trees are comprised of nodes that have children nodes and a cascading effect is met with data storage. The top most node is called the root and has a value. The branching structure can be traversed and it's height can be calculated.

## What does a tree look like in Python?
```py
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

## Real World Application / Problem
One example of trees being used to compute very large amounts of data in real life is a file system. Files in folders in folders is an excellent practicve problem to try to solve using trees in Python.

## Solution to Real World Application

```py
def insert(self, data):
    if self.root is None:
        self.root = BST.Node(data)
    else:
        self._insert(data, self.root) # Start at the root

```

## Problem solving (solo experience)

[Solution](solution.md)

### Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Linked Lists](linked_lists.md)
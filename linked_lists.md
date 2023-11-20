# Intro to Linked Lists
Intro material

## What does a linked list look like in Python?
```py
def __init__(self, data):
    self.data = data
    self.next_node = None
    self.prev_node = None
```

## Real World Application / Problem
Problem solving (with tutorial)

## Solution to Real World Application

```py
def replace(self, old_value, new_value):
    current = self.head
    while current is not None:
        if current.data == old_value:
            current.data = new_value
        current = current.next
```

## Problem solving (solo experience)

[Solution](solution.md)


### Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Trees](trees.md)
# Intro to Trees
Intro material

## What does a tree look like in Python?
```py
def __init__(self, data):
    self.data = data
    self.next_node = None
    self.prev_node = None
```

## Real World Application / Problem
One example of trees being used to compute very large amounts of data in real life is a database that contains the names and classification of every living creature. This naming system is called binomial nomenclature. 

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
- [Linked Lists](linked_lists.md)
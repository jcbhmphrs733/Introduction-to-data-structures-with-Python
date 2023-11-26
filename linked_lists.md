# Intro to Linked Lists
Linked lists are nodes of data that carry information or data about themselves and also two locations or addresses of memory guiding the computer to the previous and the next nodes in the data structure.

## What does a linked list look like in Python?
```py
def __init__(self, data):
    self.data = data
    self.next_node = None
    self.prev_node = None
```

## Real World Application / Problem
One real world problem that we can solve with linked lists is a simple navigation program. When you ask a GPS to plan a route for you, it can be accomplished by linking steps in a route with a linked list.
```py
def add_step(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
    else:
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
```

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

additional problem solving--


### Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Trees](trees.md)
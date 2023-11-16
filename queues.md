# Intro to Queues
Intro to queues

## What is a Queue?
Queues are useful when dealing with data that has to deal with priority. A well known characteristic of queues is First In First Out (FIFO).
```py
    queue = [5, 7, 2, 4]
```

## Real World Application / Problem
Problem solving (with tutorial)

## Solution to Real World Application

```py
def dequeue(self):
    if len(self.queue) == 0:
        print("The queue is empty.")
        return None
    for index in range(len(self.queue)):
        del self.queue[high_pri_index]
    return value
```

## Problem solving (solo experience)

[Solution](solution.md)

```py
def dequeue(self):
    if len(self.queue) == 0:
        print("The queue is empty.")
        return None
    for index in range(len(self.queue)):
        del self.queue[high_pri_index]
    return value
```

### Navigation
- [Welcome Page](welcome.md)
- [Linked Lists](linked_lists.md)
- [Trees](trees.md)

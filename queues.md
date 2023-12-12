# Intro to Queues
Queues are a fundamental data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear and removed from the front, making it an efficient choice for tasks such as managing tasks, processing requests, and more.

### Example of a Queue in Python:
```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```
### Basic Queue Operations:

| Operation       | Performance | Explanation |
| --------------- |:-----------:| ----------- | 
| Enqueue         | O(1)        | Adds an element to the rear of the queue.
| Dequeue         | O(1)        | Removes the element from the front of the queue.
| Is Empty        | O(1)        | Checks if the queue is empty.
| Size            | O(1)        | Returns the number of elements in the queue.



### Real World Problem: **** 
The real world problem we will be solving is how to pair together online players waiting in a queue for an opponent.

## Solution to Real World Application

```py
def pair_players(queue):
        paired_players = []
    
    # Sort the queue based on skill level
    sorted_players = list(queue.queue)

    while len(sorted_players) >= 2:
        player1 = sorted_players.pop(0)
        player2 = sorted_players.pop(0)
        pair = (player1, player2)
        paired_players.append(pair)
    return paired_players
```

## Problem solving (solo experience)

additional problem solving--

### Navigation
- [Welcome Page](welcome.md)
- [Linked Lists](linked_lists.md)
- [Trees](trees.md)

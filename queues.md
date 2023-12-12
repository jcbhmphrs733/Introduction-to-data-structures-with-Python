# Intro to Queues
Queues are a fundamental data structure that follows the First-In-First-Out (FIFO) principle. Elements are added at the rear and removed from the front, making it an efficient choice for tasks such as managing tasks, processing requests, and more.

![queues_img](images\queues.png)

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



## Real World Problem: Online Player Pairing 
We will use a queue to implement a program that can pair online players waiting in a queue to play a game. We will ensure that each player is paired with exactly one other player.

1. Implement a Player class with an attribute name.
2. Create a `PlayerQueue` class that can manage our queue by adding and removing players in respect to [FIFO](#intro-to-queues).
3. Create a function in the `PlayerQueue` class called `pair_players` that takes a queue of players and pairs them together.

### Solution to Real World Application

```py
class Player:
    def __init__(self, name):
        self.name = name
```
```py
class PlayerQueue:
    def __init__(self):
        self.players = []

    def enqueue_player(self, player):
        self.players.append(player)

    def dequeue_player(self):
        if not self.is_empty():
            dequeued_player = self.players.pop(0)
            return dequeued_player
        else:
            return None
        
    def pair_players(self):
        paired_players = []

        while len(players) >= 2:
            player1 = players.pop()
            player2 = players.pop()
            pair = (player1, player2)
            paired_players.append(pair)

        return paired_players
```

### Problem solving (solo experience)

On your own, try to add an attribute to the `Player` class called `skill_level`. Then add a funciton to the `PlayerQueue` class that will pair players with similar skill levels. Compare your answer to this solution [here](queues_solution.md).

## Navigation
- [Welcome Page](welcome.md)
- [Linked Lists](linked_lists.md)
- [Trees](trees.md)

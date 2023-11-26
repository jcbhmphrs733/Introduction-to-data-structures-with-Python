# What does a queue look like in Python?
Queues are useful when dealing with data that has requires attention to priority. A well known characteristic of the queue is First In First Out (FIFO). A useful python library called `queue` will help us solve a real world problem and understand how to we can apply python to the real world.

```python
    def main():
        player_queue = Queue()
```


## Real World Application / Problem
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

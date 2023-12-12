# Intro to Linked Lists
Linked lists are nodes of data that carry information or data about themselves and also two locations or addresses of memory guiding the computer to the previous and the next nodes in the data structure.

### Example of a Linked List Node in Python:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
```
### Basic Linked List Operations:

| Operation       | Performance | Explanation |
| --------------- |:-----------:| ----------- | 
| Insert Front    | O(1)        | Updates the `next_node` of the new node to point to the current head and then updating the head to the new node.
| Insert Middle   | O(n)        | Requires traversing the list to find the insertion point, and then updating the references of the neighboring nodes accordingly.
| Insert End      | O(1)        | Traverses the list until the last node is reached and updating the `next_node` of the last node to point to the new node.
| Remove Front    | O(1)        | Updates the head to point to the next node in the list, effectively disconnecting the first node.
| Remove End      | O(1)        | Traverses the list until the second-to-last node is reached and updating its `next_node` to `None`.


## Real World Problem: **Navigation System**
We will use a linked list to implement a navigation system. We will create a program that efficiently manages a route using a linked list.

1. Create a `Location` class with attributes: name (the name of the location) and `next_location` (a reference to the next location in the route).
1. Create a `NavigationList` class to manage the route, with a head attribute pointing to the starting location.
1. Create a function add_location in the `NavigationList` class to add new locations to the route.

### Solution to Real World Application:

```py
class Location:
    def __init__(self, name):
        self.name = name
        self.next_location = None
```

```py
class NavigationList:
    def __init__(self):
        self.head = None
    def add_location(self, name):
        new_location = Location(name)
        if not self.head:
            self.head = new_location
        else:
            current_location = self.head
            while current_location.next_location:
                current_location = current_location.next_location
            current_location.next_location = new_location
```

```py
# Instantiate the List
navigation_system = NavigationList()

# Add locations to the route
navigation_system.add_location("Start")
navigation_system.add_location("Office")
navigation_system.add_location("Home")
```



### Solo Problem Solving: Display Route

On your own try to add a function to the class `NavigationList` that when called, can display the Location nodes from the navigation list in order. Compare your answer to this solution [here](linked_lists_solution.md).


## Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Trees](trees.md)
# Intro to Trees
Trees are hierarchical data structures that consist of nodes connected by edges. Each node in a tree contains data and may link to other nodes, forming parent-child relationships. Trees are widely used in various applications, including file systems, hierarchical structures, and search algorithms. Trees are comprised of nodes that have children nodes and a cascading effect is met with data storage. The top most node is called the root and has a value. The branching structure can be traversed and it's height can be calculated.

## Example of a Tree in Python:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```
### Basc Tree Operations:

| Operation       | Performance | Explanation |
| --------------- |:-----------:| ----------- | 
|Insert Node	  | O(1)	    | Adds a new node to the tree.
|Delete Node	  | O(1)	    | Removes a node from the tree.
|Search Node	  | O(n)	    | Searches for a specific node in the tree.
|Traverse Tree	  | O(n)	    | Visits all nodes in the tree.



### Real World Problem: Organizational Hierarchy
We will implement an organizational hierarchy. We will create a program that will use nodes to represent an employee, and the tree structure reflects the relationships within an organization.

1. Implement an Employee class with attributes: employee_name (the name of the employee), job_title (the job title of the employee), and subordinates (a list of subordinate employees).
1. Develop an OrganizationTree class to manage the organizational structure, with a root attribute pointing to the CEO.

### Solution to Real World Application:

```py
def insert(self, data):
    if self.root is None:
        self.root = BST.Node(data)
    else:
        self._insert(data, self.root) # Start at the root

```

## Problem solving (solo experience)

[here](solution.md)

### Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Linked Lists](linked_lists.md)
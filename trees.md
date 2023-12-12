# Intro to Trees
Trees are hierarchical data structures that consist of nodes connected by edges. Each node in a tree contains data and may link to other nodes, forming parent-child relationships. Trees are widely used in various applications, including file systems, hierarchical structures, and search algorithms. Trees are comprised of nodes that have children nodes and a cascading effect is met with data storage. The top most node is called the root and has a value. The branching structure can be traversed and it's height can be calculated.

### Example of a Tree in Python:
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

### Tree Traversal Methods:
There are two common methods when searching a tree. Breadth-First Search (BFS) & Depth-First Search (DFS).

- BFS explores the tree level by level, visiting all the nodes at the current level before moving on to the next level.
BFS is often used when searching for the shortest path.
Depth-First Search (DFS):

- DFS explores the tree by going as deep as possible along each branch before backtracking. It uses recursion travers the tree. DFS is often used in tasks such as finding a path to a leaf node or exploring possibilities in a decision tree. 

The choice between BFS and DFS depends on the problem that the data structure needs solved. Each method has its advantages, and the appropriate choice will lead to more efficient solutions.

## Real World Problem: Organizational Hierarchy
We will use a tree to implement an organizational hierarchy. We will create a program that will use nodes to represent an employee, and the tree structure reflects the relationships within an organization.

1. Implement an Employee class with attributes: employee_name (the name of the employee), job_title (the job title of the employee), and subordinates (a list of subordinate employees).
1. Develop an OrganizationTree class to manage the organizational structure, with a root attribute pointing to the CEO.

### Solution to Real World Application:

```py
class Employee:
    def __init__(self, employee_name, job_title):
        self.employee_name = employee_name
        self.job_title = job_title
        self.subordinates = []

class OrganizationTree:
    def __init__(self, ceo_name, job_title):
        self.root = Employee(ceo_name, ceo_title)
```

## Solo Problem Solving: Employee Search
On your own, try to add a function to the OrganizationTree class that searches for an employee by name and returns the corresponding node. Compare your answer to this solution [here](trees_solution.md).

### Navigation
- [Welcome Page](welcome.md)
- [Queues](queues.md)
- [Linked Lists](linked_lists.md)
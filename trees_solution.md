```py
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        self.subordinates = []

    def __str__(self):
        return f"{self.name} - {self.job_title}"
```
```py
class OrganizationTree:
    def __init__(self, ceo_name, ceo_title):
        self.root = Employee(ceo_name, ceo_title)
```
```py
    def search_employee(self, employee_name, start_node=None):
        if start_node is None:
            start_node = self.root

        # Depth-first search
        stack = [start_node]
        while stack:
            current_employee = stack.pop()
            if current_employee.name == employee_name:
                return current_employee
            stack.extend(reversed(current_employee.subordinates))

        # Employee not found
        return None
```
[back](trees.md)
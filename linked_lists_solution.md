```py
class Location:
    def __init__(self, name):
        self.name = name
        self.next_location = None

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

    def print_route(self):
        current_location = self.head
        while current_location:
            print(current_location.name, end=" -> ")
            current_location = current_location.next_location
        print("End of Route")

# Instantiate the List
navigation_system = NavigationList()

# Adding locations to the route
navigation_system.add_location("Start")
navigation_system.add_location("Office")
navigation_system.add_location("Home")

# Print the route
navigation_system.print_route()
```
[back](linked_lists.md)
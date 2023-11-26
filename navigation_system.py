class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def add_step(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def display_steps(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

def main():
    navigation = LinkedList()

    # Adding steps to the navigation
    navigation.add_step("Start at home")
    navigation.add_step("Turn left at the intersection")
    navigation.add_step("Go straight for 2 blocks")
    navigation.add_step("Turn right at the traffic light")
    navigation.add_step("Arrive at your destination")

    # Displaying the navigation steps
    print("Navigation Steps:")
    navigation.display_steps()

if __name__ == "__main__":
    main()
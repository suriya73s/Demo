class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the Linked List
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    # Method to add a node at the end of Linked List
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    # Update node of a linked list at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head == None:
            return
        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node.next and current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    # Method to remove node at given index
    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return
        while(current_node != None and current_node.next and current_node.next.data != data):
            current_node = current_node.next
        if current_node != None and current_node.next != None:
            current_node.next = current_node.next.next

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size + 1
                current_node = current_node.next
        return size

    # Method to print the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# create a new linked list
llist = LinkedList()

# Display the menu options
def display_menu():
    print("\nLinked List Operations")
    print("1. Add node at the beginning")
    print("2. Add node at the end")
    print("3. Add node at specific index")
    print("4. Remove first node")
    print("5. Remove last node")
    print("6. Remove node by index")
    print("7. Remove node by value")
    print("8. Update node value at index")
    print("9. Print linked list")
    print("10. Get size of linked list")
    print("11. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-11): ")

    if choice == "1":
        data = input("Enter the data to add at the beginning: ")
        llist.insertAtBegin(data)
    elif choice == "2":
        data = input("Enter the data to add at the end: ")
        llist.insertAtEnd(data)
    elif choice == "3":
        data = input("Enter the data to add: ")
        index = int(input("Enter the index to insert at: "))
        llist.insertAtIndex(data, index)
    elif choice == "4":
        llist.remove_first_node()
        print("Removed first node.")
    elif choice == "5":
        llist.remove_last_node()
        print("Removed last node.")
    elif choice == "6":
        index = int(input("Enter the index to remove the node: "))
        llist.remove_at_index(index)
    elif choice == "7":
        data = input("Enter the value of the node to remove: ")
        llist.remove_node(data)
    elif choice == "8":
        index = int(input("Enter the index to update: "))
        val = input("Enter the new value: ")
        llist.updateNode(val, index)
    elif choice == "9":
        print("Linked List:")
        llist.printLL()
    elif choice == "10":
        print("Size of linked list:", llist.sizeOfLL())
    elif choice == "11":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

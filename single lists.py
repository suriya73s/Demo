class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    def remove_first_node(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        current_node = self.head
        while(current_node.next and current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return

        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def remove_node(self, data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            return

        while(current_node != None and current_node.next and current_node.next.data != data):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def printLL(self):
        current_node = self.head
        if not current_node:
            print("The linked list is empty.")
        else:
            while current_node:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None")

# Function to interact dynamically with the user
def dynamic_operations():
    llist = LinkedList()
    while True:
        print("\nLinked List Operations:")
        print("1. Insert multiple values at beginning")
        print("2. Insert multiple values at index")
        print("3. Insert multiple values at end")
        print("4. Remove first node")
        print("5. Remove last node")
        print("6. Remove node by index")
        print("7. Remove node by value")
        print("8. Update node by index")
        print("9. Print linked list")
        print("10. Get size of linked list")
        print("11. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            data = input("Enter multiple values to insert at the beginning (separate with spaces): ").split()
            for value in data:
                llist.insertAtBegin(value)
            print(f"Inserted {len(data)} values at the beginning.")
        elif choice == 2:
            data = input("Enter multiple values to insert at the index (separate with spaces): ").split()
            index = int(input("Enter index: "))
            for value in data:
                llist.insertAtIndex(value, index)
            print(f"Inserted {len(data)} values at index {index}.")
        elif choice == 3:
            data = input("Enter multiple values to insert at the end (separate with spaces): ").split()
            for value in data:
                llist.insertAtEnd(value)
            print(f"Inserted {len(data)} values at the end.")
        elif choice == 4:
            llist.remove_first_node()
            print("First node removed.")
        elif choice == 5:
            llist.remove_last_node()
            print("Last node removed.")
        elif choice == 6:
            index = int(input("Enter index to remove node: "))
            llist.remove_at_index(index)
            print(f"Node at index {index} removed.")
        elif choice == 7:
            data = input("Enter node value to remove: ")
            llist.remove_node(data)
            print(f"Node with data '{data}' removed.")
        elif choice == 8:
            index = int(input("Enter index to update node: "))
            new_data = input("Enter new data: ")
            llist.updateNode(new_data, index)
            print(f"Node at index {index} updated with data '{new_data}'.")
        elif choice == 9:
            print("\nCurrent Linked List:")
            llist.printLL()
        elif choice == 10:
            print(f"Size of linked list: {llist.sizeOfLL()}")
        elif choice == 11:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

# Running the dynamic interaction
dynamic_operations()

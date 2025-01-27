class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is not empty")

    def InsertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

def dynamic_operations():
    NewDoublyLinkedList = doublyLinkedList()

    while True:
        print("\nDoubly Linked List Operations:")
        print("1. Insert to Empty List")
        print("2. Insert at End")
        print("3. Delete from Start")
        print("4. Delete from End")
        print("5. Display List")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            data = input("Enter the element to insert into the empty list: ")
            NewDoublyLinkedList.InsertToEmptyList(data)
        elif choice == '2':
            data = input("Enter the element to insert at the end: ")
            NewDoublyLinkedList.InsertToEnd(data)
        elif choice == '3':
            NewDoublyLinkedList.DeleteAtStart()
        elif choice == '4':
            NewDoublyLinkedList.delete_at_end()
        elif choice == '5':
            NewDoublyLinkedList.Display()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the dynamic operations
dynamic_operations()

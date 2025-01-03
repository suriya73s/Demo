queue = []
n = int(input("Enter the number of elements to enqueue: "))
for _ in range(n):
    element = input("Enter an element to enqueue: ")
    queue.append(element)
print("\nInitial queue:")
print(queue)
m = int(input("\nEnter the number of elements to dequeue: "))
print("\nElements dequeued from queue:")
for _ in range(m):
    if queue:
        print(queue.pop(0))
    else:
        print("Queue is empty!")
print("\nQueue after removing elements:")
print(queue)

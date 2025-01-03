from collections import deque
q = deque()
n = int(input("Enter the number of elements to enqueue: "))
for _ in range(n):
    element = input("Enter an element to enqueue: ")
    q.append(element)
print("\nInitial queue:")
print(q)
m = int(input("\nEnter the number of elements to dequeue: "))
print("\nElements dequeued from the queue:")
for _ in range(m):
    if q:
        print(q.popleft())
    else:
        print("Queue is empty!")
print("\nQueue after removing elements:")
print(q)

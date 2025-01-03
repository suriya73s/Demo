from queue import Queue
max_size = int(input("Enter the maximum size of the queue: "))
q = Queue(maxsize=max_size)
n = int(input(f"Enter the number of elements to enqueue (up to {max_size}): "))
for _ in range(n):
    element = input("Enter an element to enqueue: ")
    if not q.full():
        q.put(element)
    else:
        print("Queue is full! Cannot enqueue more elements.")
print("\nQueue size after enqueuing elements:", q.qsize())
print("Full:", q.full())
m = int(input("\nEnter the number of elements to dequeue: "))
print("\nElements dequeued from the queue:")
for _ in range(m):
    if not q.empty():
        print(q.get())
    else:
        print("Queue is empty! No more elements to dequeue.")
print("\nEmpty:", q.empty())
if not q.full():
    q.put(input("\nEnter one more element to enqueue: "))
print("\nEmpty:", q.empty())
print("Full:", q.full())


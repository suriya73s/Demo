stack = []
n = int(input("Enter the number of elements to push onto the stack: "))
for _ in range(n):
    element = input("Enter an element to push onto the stack: ")
    stack.append(element)
print('\nInitial stack:')
print(stack)
m = int(input("\nEnter the number of elements to pop from the stack: "))
print('\nElements popped from stack:')
for _ in range(m):
    if stack:  
        print(stack.pop())
    else:
        print("Stack is empty!")
print('\nStack after elements are popped:')
print(stack)

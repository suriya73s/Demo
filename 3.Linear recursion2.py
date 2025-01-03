L = [1, 2, 3, 4, 5, 6, 7]
key = int(input("enter the number :"))
print('List : ', L)
def linear_search(L, key, i):
    if i >= len(L):
        return print("Element is Not present")
    if L[i] == key:
        return print(f'Element {key} is available on index : {i}')
    return linear_search(L, key, i + 1)
x = linear_search(L, key, 0)







Source Code:

def merge_sort(arr):

    if len(arr) <= 1:

        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    return merge(left, right)



def merge(left, right):

    merged = []

    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:

            merged.append(left[i])

            i += 1

        else:

            merged.append(right[j])

            j += 1

    # Add remaining elements

    merged += left[i:]

    merged += right[j:]

    return merged



# Example usage

arr = [38, 27, 43, 3, 9, 82, 10]

print("Before sorting:", arr)

sorted_arr = merge_sort(arr)

print("After sorting:", sorted_arr)


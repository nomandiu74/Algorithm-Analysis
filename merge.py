# Merge Sort in Python

def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle of the array
    mid = len(arr) // 2

    # Recursively split the array into two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two halves and return the sorted array
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge the two arrays until one of them is empty
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If there are remaining elements in the left or right array, add them
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

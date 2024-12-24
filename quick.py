# Quick Sort in Python (Beginner-friendly version)

def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (we'll use the last element in this example)
    pivot = arr[-1]

    # Create two sub-arrays (without list comprehensions)
    left = []   # Elements less than or equal to the pivot
    right = []  # Elements greater than the pivot

    # Loop through the array (excluding the pivot)
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)   # Add to left if the element is less than or equal to the pivot
        else:
            right.append(x)  # Add to right if the element is greater than the pivot

    # Recursively apply quick_sort on both sub-arrays, then combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

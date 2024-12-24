# Function to heapify a subtree rooted with node i (makes sure it's a max heap)
def heapify(arr, n, i):
    largest = i  # Assume the root (i) is the largest
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If the left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If the right child exists and is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

# Main function to do heap sort
def heap_sort(arr):
    n = len(arr)

    # Build a max heap (start from the middle of the array and work backwards)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Swap the root (largest) with the last element
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify the reduced heap (ignoring the last sorted element)
        heapify(arr, i, 0)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr)
print("Sorted array:", arr)

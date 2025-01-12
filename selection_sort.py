def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    
    Parameters:
    arr (list): List of elements to be sorted.
    
    Returns:
    list: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        # Find the index of the smallest element in the remaining unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    print("Original array:", sample_array)
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)

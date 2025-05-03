def text_to_arr(txt):
    
    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr = [int(x) for x in content[-1].split()]
    return arr

def quick_sort(arr):
    """
    Sorts a list using the Quicksort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        A new sorted list.  (Note: This implementation creates new lists)
    """
    if len(arr) <= 1:
        return arr  # Base case: an empty or single-element list is already sorted
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        left = [x for x in arr[1:] if x < pivot]  # Elements less than the pivot
        right = [x for x in arr[1:] if x >= pivot] # Elements greater than or equal to the pivot
        return quicksort(left) + [pivot] + quicksort(right) # Recursive calls and concatenation

def quicksort_in_place(arr, low, high):
    """Sorts a list in place using the Quicksort algorithm.

    Args:
        arr: The list to be sorted.
        low: The starting index of the partition to sort.
        high: The ending index of the partition to sort.
    """
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quicksort_in_place(arr, low, pi - 1)  # Sort the left partition
        quicksort_in_place(arr, pi + 1, high) # Sort the right partition

def partition(arr, low, high):
    """Partitions the list for Quicksort (in-place).

    Args:
        arr: The list to be partitioned.
        low: The starting index of the partition.
        high: The ending index of the partition.

    Returns:
        The index of the pivot after partitioning.
    """
    pivot = arr[high]  # Pivot element is the last element
    i = (low - 1)  # Index of smaller element
    #  and indicates the right position of pivot found so far

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap pivot to its correct position
    return (i + 1)


final_res = quick_sort(text_to_arr("rosalind_qs.txt"))
for i in final_res:
    print(i, end = " ")

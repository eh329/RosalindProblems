def read_hp(txt):
    file = open(txt, "r")
    n, arr = [x.strip() for x in file.readlines()]
    file.close()

    return [int(x) for x in arr.split()]

def heapify(heap, i):
    """Maintain max heap property by comparing element at index i with its parent
    and swapping if necessary, then recursively fixing the heap property upward."""
    if i == 0:
        return  # At root, nothing to do
    
    parent = (i - 1) // 2
    child = i
    
    # If child is greater than parent, swap them to maintain max heap property
    if heap[child] > heap[parent]:
        heap[parent], heap[child] = heap[child], heap[parent]
        # Continue heapifying up the tree after swapping
        heapify(heap, parent)
    # If parent is already greater than or equal to child, heap property is satisfied
    # No need to do anything else


def heap(arr):
    """
    Given: A positive integer n≤10^5 and array A[1..n] of integers from −10^5
    to 10^5.

    Return: A permuted array A
    satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
    """
    heap = []
    
    for i, x in enumerate(arr):
        heap.append(x)
        heapify(heap, i)
        
    return heap

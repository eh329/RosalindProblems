def read_dataset_from_file(filename):
    """
    Reads the dataset from a text file.
    Returns a list of arrays.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    k, n = map(int, lines[0].strip().split())
    arrays = [list(map(int, line.strip().split())) for line in lines[1:k + 1]]
    return arrays


def find_three_sum_zero(arr):
    """
    Finds one triplet of indices (1-based) p < q < r such that
    A[p] + A[q] + A[r] == 0.
    Returns the indices as a string, or '-1' if no such triplet exists.
    """
    n = len(arr)
    indexed_arr = list(enumerate(arr))  # (index, value) pairs
    indexed_arr.sort(key=lambda x: x[1])  # Sort by value

    for i in range(n - 2):
        a_idx, a_val = indexed_arr[i]
        left = i + 1
        right = n - 1
        while left < right:
            b_idx, b_val = indexed_arr[left]
            c_idx, c_val = indexed_arr[right]
            total = a_val + b_val + c_val

            if total == 0:
                # Ensure output order is p < q < r
                return " ".join(map(str, sorted([a_idx + 1, b_idx + 1, c_idx + 1])))
            elif total < 0:
                left += 1
            else:
                right -= 1

    return "-1"


def process_arrays_from_file(filename):
    arrays = read_dataset_from_file(filename)
    for arr in arrays:
        result = find_three_sum_zero(arr)
        print(result)

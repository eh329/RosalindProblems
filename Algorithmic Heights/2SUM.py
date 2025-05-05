def read_dataset_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    k, n = map(int, lines[0].strip().split())

    arrays = []
    for i in range(1, k + 1):
        arr = list(map(int, lines[i].strip().split()))
        arrays.append(arr)

    return k, n, arrays

def find_opposite_pair(arr):
    seen = {}
    for i, num in enumerate(arr):
        if -num in seen:
            return f"{seen[-num] + 1} {i + 1}"  
        if num not in seen:
            seen[num] = i
    return "-1"

def process_arrays_from_file(filename):
    k, n, arrays = read_dataset_from_file(filename)
    for arr in arrays:
        print(find_opposite_pair(arr))


dataset_file = "rosalind_2sum.txt" 
process_arrays_from_file(dataset_file)

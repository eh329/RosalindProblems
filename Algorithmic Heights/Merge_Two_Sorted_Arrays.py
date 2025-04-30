def merge_arrays(txt):
	"""
	Given: A positive integer n≤105 and an array A[1..n] of integers from −105
		   to 105.

	Return: A sorted array A[1..n].
	"""

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr1 = [int(x) for x in content[1].split()]
    arr2 = [int(x) for x in content[-1].split()]
    arr3 = []

    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0 

    while (i < n) and (j < m):

        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1

        else:
            arr3.append(arr2[j]) 
            j += 1

    while (i < n):
        arr3.append(arr1[i])
        i += 1

    while (j < m):
        arr3.append(arr2[j])
        j += 1

    for z in arr3:
        print(z, end = " ")
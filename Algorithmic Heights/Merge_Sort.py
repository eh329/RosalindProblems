def get_arr(txt):

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr = [int(x) for x in content[-1].split()]

    return arr


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merger(left, right)



def merger(left, right):

    res = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res   
	
	
final = merge_sort(get_arr("rosalind_ms.txt"))
for i in final:
    print(i, end = " ")
def three_way_part(txt):
    """
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n
    such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
    """

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr = [int(x) for x in content[-1].split()]

    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    smaller = []
    equal = []
    higher = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            smaller.append(arr[i])

        elif arr[i] == pivot:
            equal.append(arr[i])

        else:
            higher.append(arr[i])

    equal.append(pivot)

    final = smaller + equal + higher

    for j in final:
        print(j, end = " ")

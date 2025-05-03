def quic_part(txt):

    """
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
    Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n
    such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.
    """

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr = [int(x) for x in content[-1].split()]

    pivot = arr[0]
    smaller = []
    higher = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])

        else:
            higher.append(arr[i])

    smaller.append(pivot)

    final = smaller + higher
    
    for j in final:
        print(j, end = " ")

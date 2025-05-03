def text_read(txt):

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    arr = [int(x) for x in content[1].split()]
    med = int(content[-1])

    return arr, med

def median(arr, tar):
    """
    Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.
    Return: The k-th smallest element of A.
    """

    final = sorted(arr)
    return final[tar- 1]

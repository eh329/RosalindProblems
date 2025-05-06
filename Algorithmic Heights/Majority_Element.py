from collections import Counter


def read_file(txt):

    file = open(txt, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    n , k = [int(x) for x in content[0].split()]
    arrs = [[int(y) for y in x.split()] for x in content[1:]]

    return n, k, arrs

def majority_elm(n, k , arrs):
    """
    Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n
    containing positive integers not exceeding 105.

    Return: For each array, output an element of this array occurring strictly more than n/2
    times if such element exists, and "-1" otherwise.
    """

    for i in arrs:

        count = Counter(i)
        max_count = max(count.items(), key =  lambda x: x[-1])

        if max_count[-1] > (k // 2):
            print(max_count[0], end = " ")
        
        else:
            print(-1, end = " ")

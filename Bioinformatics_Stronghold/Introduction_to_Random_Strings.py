from math import log

def read_txt(text):
    file = open(text, "r")
    seq, nums = [x.strip() for x in file.readlines()]
    final_nums = [float(x) for x in nums.split(" ")]
    file.close()

    return seq, final_nums

def random_str(s, n):
    """
    Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
    Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a 
    random string constructed with the GC-content found in A[k] will match s exactly.
    """

    result = []

    for i in n:
        
        gc = i
        ta = 1 - gc
        g = c = gc / 2
        a = t = ta / 2
        total = 1

        for j in s:
            if (j == "A") or (j == "T"):
                total *= a

            else:
                total *= g

        result.append(round(log(total, 10), 3))

    for i in result:
        print(i, end = " ")

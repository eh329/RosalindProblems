def read_txt(txt):

    file = open(txt, "r")
    seq1, seq2 = [line.strip() for line in file.readlines()]
    file.close()

    return seq1, seq2

def hamming(s1, s2):
    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    """
    return sum([x1 != x2 for (x1, x2) in zip(s1, s2)])

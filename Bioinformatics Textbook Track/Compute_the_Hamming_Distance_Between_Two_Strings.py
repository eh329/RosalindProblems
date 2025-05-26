def read_seqs(txt):

    file = open(txt, "r")
    seq1, seq2 = [x.strip() for x in file.readlines()]
    file.close()

    return seq1, seq2

def hamming(s1, s2):
    """
    Given: Two DNA strings.
    Return: An integer value representing the Hamming distance.
    """

    length = len(s1)
    ham_dis = 0

    for i in range(0, length):
        if s1[i] != s2[i]:
            ham_dis += 1

    return ham_dis

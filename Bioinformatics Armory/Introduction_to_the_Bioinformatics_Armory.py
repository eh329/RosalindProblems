from collections import Counter

def seq_read(txt):

    file = open(txt, "r")
    sequence_read = [x.strip() for x in file.readlines()][0]
    file.close()
    return sequence_read

def seq_counter(seqs):
    """
    Given: A DNA string s of length at most 1000 bp.

    Return: Four integers (separated by spaces) representing the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.   
    Note: You must provide your answer in the format shown in the sample output below.
    """

    seq_count = Counter(seqs)
    bases = ["A", "C", "G", "T"]

    for i in bases:
        print(seq_count[i], end = " ")

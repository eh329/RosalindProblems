# Pass the text file from website to read_txt
# Then pass the read_txt(rosalind.txt) as argument to nuc_frequency

from collections import Counter

def read_txt(textfile):
    """
    This function reads the text file in the directory. The only input, is the name 
    of the file.
    """
    bases = ["A", "T", "C", "G"]
    seq = open(textfile, "r")
    seq_read = seq.readlines()
    seq.close()
    return "".join([nuc for nuc in seq_read[0] if nuc in bases])


def nuc_frequency(seq):
    """
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that 
    the symbols 'A', 'C', 'G', and 'T' occur in s.
    """      
    return Counter(seq).values()

# Pass the text file from website to read_txt
# Then we pass the read_txt(rosalind.txt) as argument to the next function

rev_bases = {"A": "T", "T": "A", "G": "C", "C": "G"}

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


def rev_complement(DNAseq):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    """
    return "".join([rev_bases[nuc] for nuc in DNAseq][::-1])

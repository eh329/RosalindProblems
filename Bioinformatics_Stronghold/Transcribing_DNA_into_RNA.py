# Pass the text file from website to read_txt
# Then we pass the read_txt(rosalind.txt) as argument to the next function

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


def transcribe(DNAseq):
    """
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    """
    return DNAseq.replace("T", "U")



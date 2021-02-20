def read_fasta(fastatxt):
    seq = open(fastatxt, "r")
    seq_read = seq.readlines()
    seq.close()
    return "".join([nuc for nuc in seq_read]).split("\n")


def mutation(seq):
    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).
    """
    mutation = 0

    for pos, nuc in enumerate(seq[0]):
        if nuc != seq[1][pos]:
            mutation += 1
        
        else:
            continue
            
    return mutation

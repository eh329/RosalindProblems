# Pass the name of the text file to read_fasta
# Pass read_fasta as argument to the next function

def read_fasta(fastatxt):
    seq = open(fastatxt, "r")
    seq_read = seq.readlines()
    seq.close()
    return "".join([nuc for nuc in seq_read]).split("\n")  


def gc_content(fastaseq):
    """
    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
    Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
    """
    keys = [key for key in fastaseq if ">" in key]
    
    content = {}
    sequence = ""

    for seq in fastaseq:
        if seq.startswith(">"):
            sequence = seq
            content[sequence] = ""
        
        else:
            content[sequence] += seq
    
    values = [((gc.count("C") + gc.count("G")) / len(gc)) * 100 for gc in content.values()]
    return [tup for tup in zip(keys, values)]

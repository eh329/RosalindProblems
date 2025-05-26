bases = {"A": "T", "C": "G", "T": "A", "G": "C"}

def read_txt(text):

    with open(text, "r") as file:
        sequence = [x.strip() for x in file.readlines()][0]

    return sequence

def reverse_complement(seq):
    """
    Given: A DNA string Pattern.
    Return: Pattern, the reverse complement of Pattern.
    """
    
    return "".join([bases[x] for x in seq][::-1])

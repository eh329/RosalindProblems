def read_fasta(txt):
    
    with open(txt, "r") as file:
        fasta = [line.strip() for line in file if not line.startswith(">")]
    return ''.join(fasta)

def reverse_pal(sub_seq):

    bases = {"A": "T",
            "T": "A",
            "C": "G",
            "G": "C"}
    
    return "".join([bases[x] for x in reversed(sub_seq)])

def rest_site(seq):
    """
    Given: A DNA string of length at most 1 kbp in FASTA format.
    Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
    You may return these pairs in any order.
   """

    res = []

    for i in range(0, len(seq)):
        for j in range(4, 13):

            sub = seq[i: i + j]

            if len(sub) < j:
                continue
            
            rev_pal = reverse_pal(sub)

            if sub == rev_pal:
                res.append((i + 1, j))

    return res



final = rest_site(read_fasta("rosalind_revp.txt"))
for pos, length in final:
    print(pos, length)


codon_counts = {
        'A': 4,  # Alanine: GCA, GCC, GCG, GCU
        'C': 2,  # Cysteine: UGC, UGU
        'D': 2,  # Aspartic acid: GAC, GAU
        'E': 2,  # Glutamic acid: GAA, GAG
        'F': 2,  # Phenylalanine: UUC, UUU
        'G': 4,  # Glycine: GGA, GGC, GGG, GGU
        'H': 2,  # Histidine: CAC, CAU
        'I': 3,  # Isoleucine: AUA, AUC, AUU
        'K': 2,  # Lysine: AAA, AAG
        'L': 6,  # Leucine: CUA, CUC, CUG, CUU, UUA, UUG
        'M': 1,  # Methionine: AUG (start codon)
        'N': 2,  # Asparagine: AAC, AAU
        'P': 4,  # Proline: CCA, CCC, CCG, CCU
        'Q': 2,  # Glutamine: CAA, CAG
        'R': 6,  # Arginine: AGA, AGG, CGA, CGC, CGG, CGU
        'S': 6,  # Serine: AGC, AGU, UCA, UCC, UCG, UCU
        'T': 4,  # Threonine: ACA, ACC, ACG, ACU
        'V': 4,  # Valine: GUA, GUC, GUG, GUU
        'W': 1,  # Tryptophan: UGG
        'Y': 2,  # Tyrosine: UAC, UAU
        'STOP': 3  # Stop codons: UAA, UAG, UGA
    }


def read_text(txt):
    seq = open(txt, "r")
    seq_read = [x.strip() for x in seq.readlines()][0]
    seq.close()
    return seq_read  


def mrna_infference(prot):
    """
    Given: A protein string of length at most 1000 aa.
    Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
    (Don't neglect the importance of the stop codon in protein translation.)
    """
    
    mrna = 3

    for i in prot:
        mrna *= codon_counts[i]

    return mrna  % 1000000

import re

RNA_Codons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
}


def read_fasta(txt):

    with open(txt, "r") as f:
        fasta = {}
        label = None
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                label = line[1:]
                fasta[label] = ""
            else:
                fasta[label] += line
              
    keys = list(fasta.keys())
    dna = fasta[keys[0]]
    introns = [fasta[k] for k in keys[1:]]
    return dna, introns


def rna_conversion(dna):

    return dna.replace("T", "U")

def rna_splicing(dna, introns):
    """
    Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s
           acting as introns. All strings are given in FASTA format.

    Return: A protein string resulting from transcribing and translating the exons of s. 
    """

    for sub in introns:
        pattern = re.compile(sub)
        dna = re.sub(pattern, "", dna)

    rna = rna_conversion(dna)

    protein = ""
    s = 0
    end = 3

    for i in range(0, len(rna) // 3):
        amino = RNA_Codons[rna[s:end]]
        protein += amino
        s += 3
        end += 3

    return protein

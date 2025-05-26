def read_txt(text):

    file = open(text, "r")
    k, string = [x.strip() for x in file.readlines()]
    file.close()

    return int(k), string

def kmer_generator(k, seq):
    """
    Given: An integer k and a string Text.
    Return: Compositionk(Text) (the k-mers can be provided in any order).
    """
    
    end = len(seq) - k + 1
    kmers = []

    for i in range(0, end):

        kmer = seq[i:k]
        if kmer not in kmers:
            kmers.append(kmer)

        k += 1

    kmers.sort()
    
    return kmers

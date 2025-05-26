import itertools

def read_txt(text):

    with open(text, "r") as file:
        sequence, k = [x.strip() for x in file.readlines()]

    return sequence, int(k)

def count_array(k):

    alphabet = ['A', 'C', 'G', 'T']
    kmers = sorted({''.join(p) for p in itertools.product(alphabet, repeat = k)})
    kmers_freq = {x: 0 for x in kmers}
    return kmers_freq

def frequency_array(seq, k):
    """
    Given: A DNA string Text and an integer k.
    Return: The frequency array of k-mers in Text.
    """
    
    end = len(seq) - k + 1
    count = count_array(k)

    for i in range(0, end):
        kmer = seq[i: k]

        if kmer in count:
            count[kmer] += 1

        k += 1

    return count.values()

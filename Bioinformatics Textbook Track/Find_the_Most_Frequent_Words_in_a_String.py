def read_txt(text):

    with open(text, "r") as file:
        sequence, k = [x.strip() for x in file.readlines()]

    return sequence, int(k)

def most_frequent(seq, k):
    """
    Given: A DNA string Text and an integer k.
    Return: All most frequent k-mers in Text (in any order).
    """
    
    end = len(seq) - k + 1
    count = {}

    for i in range(0, end):
        kmer = seq[i: k]

        if kmer in count:
            count[kmer] += 1

        else:
            count[kmer] = 1

        k += 1

    result = [x for x, y in count.items() if y == max(count.values())]

    return result

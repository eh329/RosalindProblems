def read_txt(text):

    with open(text, "r") as file:
        pattern, sequence = [x.strip() for x in file.readlines()]

    return pattern, sequence


def occurrences_index(pattern, sequence):
    """
    Given: Strings Pattern and Genome.
    Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
    """ 
    end = len(sequence)
    index = []

    for i in range(0, end):
        if sequence[i:].startswith(pattern):
            index.append(i)

    return index

mass_table = {"A": 71.03711,
"C": 103.00919,
"D": 115.02694,
"E": 129.04259,
"F": 147.06841,
"G": 57.02146,
"H": 137.05891,
"I": 113.08406,
"K": 128.09496,
"L": 113.08406,
"M": 131.04049,
"N": 114.04293,
"P": 97.05276,
"Q": 128.05858,
"R": 156.10111,
"S": 87.03203,
"T": 101.04768,
"V": 99.06841,
"W": 186.07931,
"Y": 163.06333}


def read_txt(txt):

    file = open(txt, "r")
    seq = [x.strip() for x in file.readlines()][0]
    file.close()
    return seq


def protein_mass(prot):
    """
    Given: A protein string P of length at most 1000 aa.
    Return: The total weight of P.
    """

    weight = 0

    for i in prot:
        weight += mass_table[i]

    return round(weight, 3)

# Just pass the text file to this function

import re

def read_str(txt):
    file = open(txt, "r")
    s, k = [x.strip() for x in file.readlines()]
    file.close()

    return s, k

def find_motif(s, k):
    """
    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.
    """
    pattern = re.compile(k)
    r = pattern.search(s)

    if not r: 
        print(-1)
        
    while r:
        indecis = r.start() 
        print(indecis + 1, end = " ")
        r = pattern.search(s, r.start() + 1)

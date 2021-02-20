# Just pass the text file to this function

def substring(text):
    """
    Given: Two DNA strings s and t (each of length at most 1 kbp).
    Return: All locations of t as a substring of s.
    """
    file = open(text, "r")
    final = file.readlines()
    string = final[0].split("\n")[0]
    substring = final[1].split("\n")[0]
    
    for number in [index + 1 for index in range(len(string)) if s.startswith(substring, index)]:
            print(number, end = " ")

def dict_counter(text_file):
    """
    Given: A string s of length at most 10000 letters.
    Return: The number of occurrences of each word in s, 
    where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
    """
    file = open(text_file, "r")
    counter = file.readlines()
    file.close()
    
    dictionary = {letter: counter[0].count(letter) for letter in counter[0]. split()}
    for key, value in dictionary.items():
        print(key, value)

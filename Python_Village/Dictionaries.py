def dict_counter(text_file):
    """
    Given: A string s of length at most 10000 letters.
    Return: The number of occurrences of each word in s, 
    where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
    """
    file = open(text_file, "r")
    content = file.read()  
    file.close()
    
    words = content.split()
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    for word, count in word_counts.items():
        print(word, count)

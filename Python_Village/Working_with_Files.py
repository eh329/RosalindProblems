def even_lines(text_file):
    """
    Given: A file containing at most 1000 lines.
    Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
    """
    file = open(text_file, "r")
    lines = file.readlines()
    file.close()

    for index, line in enumerate(lines, start = 1):
        if index % 2 == 0:
            print(line)

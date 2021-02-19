# Pass the name of the text file as string to the function.

def str_manipulation(text):
    """
    Given: A string s of length at most 200 letters and four integers a, b, c and d.
    Return: The slice of this string from indices a
    through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
    """
    file = open(text, "r")
    reading = file.readlines()
    file.close()
    return reading[0][int(reading[1].split()[0]): int(reading[1].split()[1]) + 1] + " " + reading[0][int(reading[1].split()[2]): int(reading[1].split()[3]) + 1]

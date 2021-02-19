def odd_sum(a, b):
    """
    Given: Two positive integers a and b (a<b<10000).
    Return: The sum of all odd integers from a through b, inclusively.
    """
    return sum([num for num in range(a, b + 1) if num % 2 != 0])

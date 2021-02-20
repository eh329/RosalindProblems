def rabbit(n, k):
    """
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, 
    if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    """
    
    if n < 2:
        return n
    
    else:
        return rabbit(n - 1, k) + (rabbit(n - 2, k) * k)

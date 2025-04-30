def memo_fib(n, memo = None):
	"""
	Given: A positive integer n≤25
	Return: The value of Fn

	"""

    if memo is None:
        memo = {}

    if (n in memo.keys()):
        return memo[n]
    
    if (n == 0):
        return 0
    
    elif (n == 1):
        return 1
    
    memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
    return memo[n]
def insertion_sort(dts):
	"""
	Given: A positive integer n≤103 and an array A[1..n] of integers.

	Return: The number of swaps performed by insertion sort algorithm on A[1..n].
	"""
    
    file = open(dts, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    nums = [int(num) for num in content[1].split()]
    swap = 0

    for i in range(1, len(nums)):
        j = i - 1

        while (j >= 0 and nums[j + 1] < nums[j]):
            tmp = nums[j + 1]
            nums[j + 1] = nums[j]
            nums[j] = tmp
            j -= 1
            swap += 1

    return swap
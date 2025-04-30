def binary_search(inp):
	"""
	Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n]
		   of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

	Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
	"""
    file = open(inp, "r")
    content = [x.strip() for x in file.readlines()]
    file.close()

    nums = [int(n) for n in content[2].split()]
    keys = [int(k) for k in content[-1].split()]

    indicies = []

    for target in keys:
        l, r = 0, len(nums) - 1
        found = False

        while (l <= r):
            mid = (l + r) // 2

            if (target < nums[mid]):
                r = mid - 1

            elif (target > nums[mid]):
                l = mid + 1

            else:
                indicies.append(mid + 1)
                found = True
                break

        if not found:
            indicies.append(-1)

    for i in indicies:
        print(i, end = " ")
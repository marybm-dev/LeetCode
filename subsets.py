def subsets(nums):
	results = [[]]
	nums.sort()
	for num in nums:
		results += [ i + [num] for i in results]
	return results
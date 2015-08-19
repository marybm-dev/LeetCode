def subsesWithDup(nums):
	results = [[]]
	nums.sort()
	for num in nums:
		results += [ i + [num] for i in results if i + [num] not in results]

	return results
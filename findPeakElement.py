def findPeakElement(nums):
	maxElement = nums[0]
	maxIndex = 0
	index = 0

	if len(nums) % 2 != 0:		# odd size list
		index = 1
	else:						# even size list
		if nums[0] < nums[1]:
			maxElement = nums[1]
			maxIndex = 1
			index = 2

	for i in range(index, len(nums)-1, 2):
		if nums[i] < nums[i+1]:
			max = nums[i+1]
			maxI = i+1
		else:
			max = nums[i]
			maxI = i

		if max > maxElement:
			maxElement = max
			maxIndex = maxI

	return maxIndex
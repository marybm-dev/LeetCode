def findMedianSortedArrays(nums1, nums2):
	mergedList = list(merge(nums1, nums2))
	median = 0

	if len(mergedList) % 2 != 0:
		median = mergedList[len(mergedList)/2]
	else:
		medA = mergedList[(len(mergedList)/2)-1]
		medB = mergedList[len(mergedList)/2]
		median = (medA + medB) / float(2)

	return median
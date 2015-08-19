import math

def reverseNum(number):
	if number < 10:
		return number
	else:
		ones = number % 10
		rest = number // 10
	return ones * 10 ** int(math.log10(rest) +1) + reverseNum(rest)
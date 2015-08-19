def rangeBitwiseAnd(m, n):
    while m < n:
    	n = n & (n-1)

    return n
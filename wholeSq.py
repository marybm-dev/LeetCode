def wholeSq(A, B):
   low = 0
   if A < 0:
       low = 0
   else:
       low = A
       
   perf_sq = 0
   for num in range(low,B):
       if math.sqrt(num).is_integer():
           perf_sq += 1
   
   return perf_sq

print wholeSq(4, 17)
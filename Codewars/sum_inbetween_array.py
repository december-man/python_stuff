get_sum = lambda a,b: (a+b)*(abs(a-b)+1)/2
#or
get_sum2 = lambda a,b: sum([i for i in range (min(a,b), max(a,b) + 1)])
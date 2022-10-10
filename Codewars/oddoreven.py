odd_or_even = lambda a: ['even', 'odd'][sum(a)%2]
print(odd_or_even([1,2,3,0,-1]))
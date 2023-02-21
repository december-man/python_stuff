#through generator expression
arrays_substractor = lambda a,b: [i for i in a if i not in b]
print(arrays_substractor([1,2,3,4,5,6,7],[1,3,5,7]))

# through filter
arrays_substractor2 = lambda a,b: list(filter(lambda i: i not in b, a))
print(arrays_substractor2([1,2,3,4,5,6,7,8,9],[2,4,6,8]))
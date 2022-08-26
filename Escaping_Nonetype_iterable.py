def compare(arr1, arr2):
    try:
        ars1 = sorted([i ** 2 for i in arr1])
        ars2 = sorted(arr2)
    except TypeError:
        return False
    else:
        return ars1==ars2
print(compare([0,2,None,3],[9,0,9,4]))
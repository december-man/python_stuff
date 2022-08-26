#my solution
def minmax_1(string1):
    return str(max([int(i) for i in string1.split(' ')])) + '' + str(min([int(i) for i in string1.split(' ')]))
# way to optimize the code 1: .format and .split with key:
def minmax_2(string):
    sortedlist = sorted(string.split(), key=int)
    return '{} {}'.format(sortedlist[-1], sortedlist[0])
#way to optimize the code 2: % string reference:
def minmax_3(string):
    sortedlist = [int(i)for i in string.split(' ')]
    return "%i %i" % (max(sortedlist),min(sortedlist))
#way to optimize the code 3: f-string:
def minmax_4(string):
    sortedlist = [int(i)for i in string.split(' ')]
    return f"{max(sortedlist)} {min(sortedlist)}"
#way to optimize the code 4: good 'ol join with function x as an object:
def minmax_5(string):
    return ' '.join(x(string.split(), key=int) for x in (max,min))
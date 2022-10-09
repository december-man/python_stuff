# PEP 3101
print('{0:_^15}'.format('hey'))
# ^ centers the {0} string element in between the '_' char before ^
print('{0:>21}'.format('SLAVA UKRAINE'))
# !r or !s to convert to str
print("{0!r:20}".format(10))
# Not obvious string unification:
print(
    
    
    'svisteli svistelki'
    
    ' sosali sosalki'

)
# obvious string unification:
print(\
'two plus two is four\
minus 1 is three\
quit maths')

# zero mod division (integer division)
4//3

#modulo %

4%3

#bitewise shifts
3 << 2 # 3 is 11 bitshift by 2 bits to the left will give 1100 which is 12
7 >> 1 # 7 is 111, bitshift by 1 bits to the right will give 11 which is 3
#bitwise logical operations
6 & 4 # 110 & 100 = 100
7 & 4 # 111 & 100 = 100
9 & 3 # 1001 & 11 = 1
12 & 7 # 1100 & 111 = 100
7 | 4 # 111 | 100 = 111
12 | 7 # 1100 | 111 = 1111
14 | 3 # 1110 | 11 = 1111
7 ^ 4 # 111 ^ 100 = 11
11 ^ 6 # 1011 ^ 110 = 1101
~100

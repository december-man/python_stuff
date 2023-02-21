from array import array
from re import findall
from re import match
from re import subn
from re import finditer
from re import compile
#counting smiley faces in the input list of randomly generated sequences of "),D,:,;,-,~"

#using regex findall
def count_objects(array): 
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(array))))
#what the fuck is 'r'?
#what the hell is '?'
#the fuck is that syntax

# using regex match
def count_objects2(array2):
    return sum(1 for s in array2 if match(r'\A[:;][-~]?[)D]\Z',s))
#what the fuck is 'r'?
#what the hell is '?'
#what the fuck is \A\Z?
#what does regex match even do?

#using regex subn
def count_objects3(array3):
    return subn('[:;][-~]?[)D]','',' '.join(array3))[1]
#what does subn even do? syntax??

#using regex finditer
def count_objects4(array4):
    return sum(1 for _ in finditer(r"[:;][-~]?[)D]", " ".join(array4)))
#what does finditer even do? syntax??

#using regex compile, match
def count_objects5(array5):
    count = 0
    for i in array5:
        p = compile("^[:;][-~]*[)D]")
        if p.match(i):
            count +=1
    return count
#what does compile do?
#what is that syntax "^*"?

#sometests

print(count_objects5([";",";^","~~",": ))",":~)"]))
        
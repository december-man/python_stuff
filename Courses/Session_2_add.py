from collections import defaultdict as dd
from itertools import combinations as cbn
from itertools import product as prod
from typing import Dict, Any, Tuple, List

def task_3(data: Dict[Any, List[str]]):
    """
    Instead, find all possible combinations (including the ones with different order)
    """
    l = []
    for k,v in data.items():
        l += [*data[k]]
    combs = [''.join(comb) for comb in set(cbn(l, len(data)))]
    return combs


data = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
data.count(data[0][1])

my_set = set([1, 2, 3, 2.0, 4, 2.5, "hello", "world"])
print(my_set)

a,b = 2, 2.0
a==b, a is b
{a,b}

array = ["flower", "flows"]
dct = {k:array[0][k] for k in range(len(array[0]))}; dct


def task_7(words: List[str]) -> str:
    """
    During one of the Q&A's it was mentioned to avoid regex & built-in string methods if the solution would be
    based fully on them.
    Lets try and implement the following idea:
    
    """
    # sanity check
    if "" in words:
        return ""
    # hashing the first word
    dct = {k:words[0][k] for k in range(len(words[0]))} 
    longest_prefix = ""
    i = 1
    while i < len(words):
        for l in words[i]:
            if l != dct[i-1]:
                return longest_prefix
            else:
                longest_prefix += dct[i-1]
                break      
        i += 1
        
def task_7(words: List[str]) -> str:
    """
    During one of the Q&A's it was mentioned to avoid regex & built-in string methods if the solution would be
    based fully on them.
    Lets try and implement the following idea:
    1. Find the shortest word in a list 
    2. Cycle through list of words checking if a slice (ascending in size) of a shortest word is present:
        if any of the words will not have it, return the shortest prefix.
    Notes: sorting with any() will decrease the chance of catching the worst case scenario for time complexity
        in a nested loop. However, sorting itself is slower then just finding the shortest string and going 
        from there. In the end I've chosen the solution with sorting.
        A word that is being searched for a prefix is also getting sliced because we need a match to be a
        prefix, not just any part of the word.
    """
    # Sorting in a descending order, LIFO pop()
    words.sort(key = len, reverse = True)
    shortest_word = words.pop()
    # sanity check
    if shortest_word == "":
        return ""
    # While loop to iterate over slices of the shortest word
    i = 1
    while i <= len(shortest_word):
        # for loop that checks for prefix presence in words is built inside the any() statement in the condition
        if any(shortest_word[:i] not in word[:i] for word in words):
            return shortest_word[:i-1] #return the previous prefix on True
        i += 1
    # return the whole shortest_word if the condition did not trigger - it is a prefix itself
    return shortest_word


def task_8(haystack: str, needle: str) -> int:
    """
    The main idea here is in the condition: just the equality between the start of the needle string and
    the element in the haystack is not enough, since we can have a 'compound' needle.
    The second mandatory condition is to check whether the haystack contains the whole needle. 
    This can be implemented using slicing.
    """
    # 0 for no-needle case:
    if needle == "":
        return 0
    i = 0
    # Cycle through elements of a haystack (letter-by-letter)
    while i < len(haystack):
        # complex condition mentioned in the docstring
        if needle[0] == haystack[i] and haystack[i:i+len(needle)] == needle:
            return i
        i += 1
    # return -1 on absence
    return -1
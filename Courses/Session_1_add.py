#imports
from typing import List

# Session 1 Solution Pool

# Task 1:

# Two-pointer method
def task_1(array: List[int], target: int) -> List[int]:
    """
      
    """
    sorted_array = sorted(array)
    # init two-pointer approach: `i` will start traversing sorted array from the left, `j` - from the right
    i = 0
    j = len(array) - 1
    while i < j:
        # if sum equals target - return the pair sorted in the original array order, since tests imply
        # the importance of order in the answer
        if (sorted_array[i] + sorted_array[j] == target):
            return sorted([sorted_array[i], sorted_array[j]], key = lambda x: array.index(x))
        # if sum is smaller than the target, we have to move to the right to bigger values with the left pointer
        elif sorted_array[i] + sorted_array[j] < target:
            i += 1 
        # if sum is bigger than the target, we have to move to the left to smaller values with the right pointer
        else:
            j -= 1
        # thus the solution converges to the pair in the middle, until i=j. If no pairs where found - return []
    return []



# Task 2
def task_2(number: int) -> int:
    """
    Oh, the pain... I had this task at some interview and answered with int(str(num)[::-1])...
    ...Little did I know.
    The solution is to isolate the digits from right to left of a base 10 number using modulo & floor division
    operators, until the given number will be reduced to 0 by the floor division.
    """
    # init
    mirror_number = 0
    abs_number = abs(number) # removing the sign to prevent incorrect `%` calculations & cycle behavior
    while abs_number > 0:
    # multiply by 10 to create another digit to the right, then add the division by 10 residue 
       mirror_number = mirror_number*10 + abs_number % 10
    # digit by digit, from right to left, until the given number will be equal to zero
       abs_number //= 10
    return mirror_number if number >= 0 else -mirror_number # returning the sign back


def task_4(string: str) -> int:
    """
    The idea is to store roman numerals and their numeric equivalent as a key:value pair in a dictionary,
    so when we cycle through a given numeral string, we add up their individual numeric values.
    The special cases of subtraction are defined by the condition of having a current numeral smaller then the
    following.
    Additional notes: 
    `continue` operator is used to skip straight to the next iteration if the i-th numeral satisfies one
    of the special conditions, so the iterator `i` won't be incremented by 1 after already being incremented by 2.
    This algorithm relies on correct input, i.e. it doesn't check the validity of the input ('IIII', 'IXL') and so on.
    """
    # init dict with roman numerals
    dct = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    i = 0
    number = int()
    while i < len(string):
        # check if the current numeral is smaller than the next one - subtract condition
        if  i < len(string) - 1 and dct[string[i+1]] > dct[string[i]]:
            number += dct.get(string[i+1]) - dct.get(string[i])
            i += 2 # skip the next numeral (because it is already included)
            continue
        # if no special cases found add the numeric equivalent of a numeral to a total sum (number)
        number += dct.get(string[i])
        i += 1
    return number
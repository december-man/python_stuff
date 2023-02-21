def multiargs(initial = 666, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(multiargs(1,3,4,5,6,7,2,5,3,34,234,24, vegetables = 23, fruits = 1, penetrations = 666))


def keyargs(i = 5, *numberz, extra_number):
    count = i
    for number in numberz:
        count += number
    count += extra_number
    return count

print(keyargs(1, 1,2,3, extra_number = 50))
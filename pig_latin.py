import string as str
import re

#doing it STANDARD way:
def pig_it(text):
    temp = []
    for i in text.split(' '):
        if i in str.punctuation:
            temp += i
        else:
            i = i[1:] + i[0] + 'ay'
            temp += i + ' '
    return (''.join([i for i in temp])).rstrip()

print(pig_it('Hooray lads ! PIGGED IT .'))

# doing it REGEX way:
def pigged_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)
print(pigged_it('Hooray lads! PIGGED IT.'))
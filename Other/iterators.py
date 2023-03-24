# a dive into python iterators
numbers = [2, 5, 8]   # iterable
iterator1 = iter(numbers)   # iterator
next(iterator1)   # 2
next(iterator1)   # 5
next(iterator1)   # 8
next(iterator1)   # error:
StopIteration

class Repeat:
   def __init__(self, msg):
     self.msg = msg
     
   def __iter__(self):
     return self
     
   def __next__(self):
     return self.msg

""" 
obj = Repeat("car")
for message in obj:
   print(message)
"""
"""
# for loop in a nutshell
obj = Repeat("car")
obj_iterator = obj.__iter__()
while True:
  message = obj_iterator.__next__()
  print(message)
"""
# building your own finite iterator
class FiniteRepeat:
   def __init__(self, msg, max_count):
     self.msg = msg
     self.max_count = max_count
     self.count = 0
     
   def __iter__(self):
     return self
     
   def __next__(self):
     if self.count >= self.max_count:
        raise StopIteration
     self.count += 1
     return self.msg
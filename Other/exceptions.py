
#basic try-except

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()


#another case with finally
f = open('myfile.txt')

try:
   print(f.read())
except:
   print("Something went wrong")
finally:
   f. close()

#raise
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
      raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

# Exception class

class InputError(Exception):
    pass
    
raise InputError('Custom exception')
# Output:
# Traceback (most recent call last):
# File "<stdin>", line 4, in <module>
# InputError: Custom exception
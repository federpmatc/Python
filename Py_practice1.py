# https://www.freecodecamp.org/news/if-name-main-python-example/
# Python module to execute

import python2
from python2 import function_four

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   python2.function_three()
   function_four()


else:
   print("File one executed when imported")

# int       Integer
# int can store Positive and Negative values. The size is depending on data
# int Immutable 

import sys

x = 1234567890233456789
print(x)
print(sys.getsizeof(x))

"""
    when we change int value it's creates new Object 
    because python doen't know the next size of value 
"""
y = 12345
print(id(y))
y = 12346
print(id(y))



















# float     Floating Paint 
# bool      Boolean
# complex   Complex Number
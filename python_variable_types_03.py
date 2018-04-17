#!/usr/bin/python3

# Data Type Conversion

# int(x [,base])
# Converts x to an integer. The base specifies the base if x is a string.
print (int(32.3e18))
print (int("100"))
print (int("100" ,8))
print (int("64" ,8))
print (int("100" ,16))
print (int("64" ,16))

print ("######################################")


# float(x)
# Converts x to a floating-point number.
print (float("-21.9"))
print (float("32.3e18"))
print (float("-32.54e100"))
print (float("70.2E12"))
print (float("70.2E125"))

print ("######################################")


# complex(real [,imag])
# Creates a complex number.

print (complex("3.14j"))
print (complex("45.j"))
print (complex("9.322e-36j"))
print (complex(".876j"))
print (complex("-.6545+0J"))
print (complex("3e+26J"))
print (complex("4.53e-7j"))

print ("######################################")


# str(x)
# Converts object x to a string representation.

print (str(3.14j))
print (str(10))
print (str(-.6545+0J))
print (str(True))

print ("######################################")


# repr(x)
# Converts object x to an expression string.

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print (repr(list))
print (repr(tuple))

print ("######################################")


# eval(str)
# Evaluates a string and returns an object.
x = 1
print (eval('x + 1'))
print (eval('x'))

print ("######################################")


# tuple(s)
# Converts s to a tuple.


# list(s)
# Converts s to a list.


# set(s)
# Converts s to a set.


# dict(d)
# Creates a dictionary. d must be a sequence of (key,value) tuples.


# frozenset(s)
# Converts s to a frozen set.


# hex(x)
# Converts an integer to a hexadecimal string.
print (hex(7))
print (hex(8))
print (hex(9))
print (hex(10))
print (hex(11))
print (hex(12))
print (hex(13))
print (hex(14))
print (hex(15))
print (hex(16))
print (hex(17))

print ("######################################")


# oct(x)
# Converts an integer to an octal string.
print (oct(7))
print (oct(8))
print (oct(9))
print (oct(10))
print (oct(11))
print (oct(12))
print (oct(13))
print (oct(14))
print (oct(15))
print (oct(16))
print (oct(17))

print ("######################################")

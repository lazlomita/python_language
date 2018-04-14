#!/usr/bin/python3

# Assigning Values to Variables
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
print (counter)
print (miles)
print (name)

print ("######################################")

# Multiple Assignment
a = b = c = 1
print (a)
print (b)
print (c)

print ("--------------------------------------")

a, b, c = 1, 2, "john"
print (a)
print (b)
print (c)

print ("######################################")

print ("######################################")

# Python Numbers
var1 = 1
var2 = 10
print (var1)
print (var2)
del var1, var2
#print (var1) # NameError: name 'var1' is not defined
#print (var2) # NameError: name 'var1' is not defined
print ("--------------------------------------")

var1 = 10
var2 = 100
var3 = -786
var4 = -0x260
var5 = 0x69
print (var1)
print (var2)
print (var3)
print (var4)
print (var5)
del var1, var2, var3, var4, var5
print ("--------------------------------------")

var1 = 0.0
var2 = 15.20
var3 = -21.9
var4 = 32.3e18
var5 = -90.
var6 = -32.54e100
var7 = 70.2E12
print (var1)
print (var2)
print (var3)
print (var4)
print (var5)
print (var6)
print (var7)
del var1, var2, var3, var4, var5, var6, var7
print ("--------------------------------------")

var1 = 3.14j
var2 = 45.j
var3 = 9.322e-36j
var4 = .876j
var5 = -.6545+0J
var6 = 3e+26J
var7 = 4.53e-7j
print (var1)
print (var2)
print (var3)
print (var4)
print (var5)
print (var6)
print (var7)
del var1, var2, var3, var4, var5, var6, var7
print ("--------------------------------------")

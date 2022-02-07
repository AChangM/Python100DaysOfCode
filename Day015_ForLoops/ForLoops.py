# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 00:33:13 2021

@author: Alfonso
"""


########################
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
    
########################

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

########################

for n in "banana":
    print(n)


###########################

s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20])

print(s[:2])

print(s[8:])

print(s[:])

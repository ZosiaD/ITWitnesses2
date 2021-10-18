'''
Write a program that asks the user to enter an input.

Print whether it is True or False
Check if an input is None or NaN and print the result of the check
'''

import math

inpuut = input('Enter an input:')
print(bool(inpuut))

if float(inpuut) is None:
    print('Input is None')
elif math.isnan(float(inpuut)):
    print('Input is Nan')

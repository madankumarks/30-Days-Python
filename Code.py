# 100days-Code-Python
#Cheat sheet

#Day-1

input_string=input()
print('Hello, World.')
print(input_string)

#Day-2

i = 4
d = 4.0
s = 'HackerRank '
a=int(input())
b=float(input())
c=str(input())
print(i+a)
print(d+b)
print(s+c)

#Day-3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):


    # Write your calculation code here
    tip = (tip_percent/100)* meal_cost # calculate tip
    tax = (tax_percent/100)* meal_cost# caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = round(meal_cost+tip+tax)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
    
    Day-4
    
    if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print('Weird')
    elif N%2==0 and N in range(1,6):
        print('Not Weird')
    elif N%2==0 and N in range(5,21):
        print('Weird')
    elif N%2==0 and N>20:
        print('Not Weird')
        
Day-5


    

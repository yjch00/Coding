import sys

def mon2day(a,b):
    
    day = 0
    
    for i in range(1,a):
        if i in [4, 6, 9, 11]:
            day += 30
        elif i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        else:
            day 
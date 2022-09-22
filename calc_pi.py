import sys
from fractions import Fraction

n = 0
arr = []
def calc_nvalue(n):
    return (n+2)

def pi_calc(n):
    for i in range (0,4):
        n = calc_nvalue(n)
        denominator = n*(n+1)*(n+2)
        val = divmod(4,denominator)
        tmp = Fraction(4,denominator)
        arr.insert(i,float(tmp))
    value = 3 + arr[0] - arr[1] + arr[2] - arr[3]
    return value 
    
pi_value = pi_calc(n)
print("Pi value is ",pi_value)

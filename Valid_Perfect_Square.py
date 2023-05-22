import math as m
t = int(input())
for i in range(t):
    n = int(input())
    sqrt = int(m.sqrt(n))
    if (sqrt*sqrt == n):
        print("True")
    else :
        print("False")
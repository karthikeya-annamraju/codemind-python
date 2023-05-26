def revs(n):
    rev = 0
    while n > 0:
        rev = (rev*10) + (n%10)
        n//=10
    return rev
    
a = int(input())
b = int(input())
for i in range(a, b+1):
    if revs(i) == i:
        print(i, end = " ")
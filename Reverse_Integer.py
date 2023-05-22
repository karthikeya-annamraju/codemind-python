def rev(a):
    n = abs(a)
    rev = 0
    while n != 0:
        rev = (rev*10) + (n%10)
        n//=10
    return rev
num = int(input())
res = rev(num)
if num < 0:
    print(int(-1*res))
else:
    print(res)
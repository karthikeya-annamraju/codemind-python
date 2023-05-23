def rev(n):
    rev = 0
    while n > 0:
        rev = (rev*10) + (n%10)
        n//=10
    return rev

t = int(input())
arr = list(map(int, input().split()))
for x in arr:
    print(rev(x), end = " ")
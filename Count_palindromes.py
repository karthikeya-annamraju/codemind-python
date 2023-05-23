def palin(n):
    rev = 0
    x = n
    while n > 0:
        rev = (rev*10) + (n%10)
        n//=10
    if x == rev:
        return True
    else:
        return False
    
t = int(input())
arr = list(map(int, input().split()))
c = 0
for k in arr:
    if palin(k):
        c+=1
print(c)
def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True
        
t = int(input())
arr = list(map(int, input().split()))
c = 0
for i in arr:
    if i == 1:
        c = -1
    if Prime(i):
        c+=1
print(c)
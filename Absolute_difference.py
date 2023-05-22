def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True

t = int(input())
arr = list(map(int, input().split()))
p = 1
np = 1
for j in arr:
    if Prime(j):
        p*=j
    else:
        np*=j
dif = np-p
print(abs(dif))
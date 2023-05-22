def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else :
        return True

t = int(input())
arr = list(map(int, input().split()))
lst = []
for k in arr:
    if k == 1:
        continue
    if Prime(k):
        lst.append(k)
        
avg = sum(lst)/len(lst)
print(format(avg, ".2f"))
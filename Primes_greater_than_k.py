def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else :
        return True

t = int(input())
arr = list(map(int, input().split()))
k = int(input())
lst = []
for j in arr:
    if j == 1:
        continue
    if j >= k and Prime(j):
        lst.append(j)
print(len(lst))
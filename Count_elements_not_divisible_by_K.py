t, k = map(int, input().split())
arr = list(map(int, input().split()))
c = 0
for x in arr:
    if x%k != 0:
        c+=1
    else:
        continue
print(c)
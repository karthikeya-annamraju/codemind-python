t = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(t):
    if i == t-1:
        continue
    if arr[i] < arr[i+1]:
        c+=1
    else:
        break
if (c == t-1):
    print("yes")
else:
    print("no")
t = int(input())
arr = list(map(int, input().split()))
earr = []
oarr = []
for i in range(t):
    if i%2 == 0:
        earr.append(arr[i])
    else:
        oarr.append(arr[i])
res = sum(oarr) - sum(earr)
if res == 0:
    print("YES")
else:
    print("NO")
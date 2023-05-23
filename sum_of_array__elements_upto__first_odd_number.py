t = int(input())
arr = list(map(int, input().split()))
s = 0
for x in arr:
    if x%2 != 0:
        break
    else:
        s = s + x
print(s)
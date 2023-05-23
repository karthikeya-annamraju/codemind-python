t = int(input())
arr = list(map(int, input().split()))
key = int(input())
s = 0
for x in range(t):
    if x != key:
        s = s + arr[x]
    else:
        break
print(s)
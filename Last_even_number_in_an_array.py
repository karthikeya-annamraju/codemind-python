t = int(input())
lst = list(map(int, input().split()))
for i in range(t):
    if lst[i]%2==0:
        s = lst[i]
print(s)
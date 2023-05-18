t = int(input())
vals = list(map(int, input().split()))
for i in range(t):
    if vals[i]%2==0:
        s = i
print(s)
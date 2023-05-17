c = 0
t = int(input())
lst = list(map(int, input().split()))
key = int(input())
for i in lst:
    if key == i:
        c+=1
print(c)
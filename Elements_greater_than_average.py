t = int(input())
arr = list(map(int, input().split()))
avg = sum(arr)//t
c = 0
for i in range(t):
    if arr[i] >= avg:
        c+=1
print(c)
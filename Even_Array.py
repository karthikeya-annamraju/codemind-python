t = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(t):
    if arr[i]%2 == 0:
        c+=1
        
if (c == t):
    print("True")
else :
    print("False")
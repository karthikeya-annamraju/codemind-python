t = int(input())
arr = list(map(int, input().split()))
for i in range(t):
    if arr[i] != 0 and arr[i] != 1:
        print("False")
        break
else:
    print("True")
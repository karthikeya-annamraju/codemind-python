t = int(input())
arr = list(map(int, input().split()))
for i in range(1, t, 2):
    if i%2 != 0 and arr[i]%2 == 0:
        print("False")
        break
else :
    print("True")
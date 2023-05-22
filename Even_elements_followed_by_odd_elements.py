t = int(input())
arr = list(map(int, input().split()))
elst = []
olst = []
for i in range(t):
    if arr[i]%2 == 0:
        elst.append(str(arr[i]))
    else:
        olst.append(str(arr[i]))
final_lst = (elst+olst)
new = " ".join(final_lst)
print(new)
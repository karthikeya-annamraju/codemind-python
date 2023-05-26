t = int(input())
arr = list(map(int, input().split()))
l_arr = []
r_arr = []
for i in range(0, t//2):
    l_arr.append(arr[i])
    
for k in range(t//2, t):
    r_arr.append(arr[k])

r_arr.reverse()
res = r_arr+l_arr
for x in res:
    print(x, end =" ")
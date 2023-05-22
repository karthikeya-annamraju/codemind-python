def unique(arr):
    ulst = []
    for x in arr:
        if x not in ulst:
            ulst.append(x)
    return ulst
    
t = int(input())
arr = list(map(int, input().split()))
res = unique(arr)
print(sum(res))
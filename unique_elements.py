def unique(arr):
    ulst = []
    for x in arr:
        if x not in ulst:
            ulst.append(x)
    for y in ulst:
        print(y, end = " ")

t = int(input())
arr = list(map(int, input().split()))
unique(arr)
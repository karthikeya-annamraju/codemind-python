n = input()
arr = list(n)
s = set(arr)
if len(arr) == len(s):
    print("Unique Number")
else:
    print("Not Unique Number")
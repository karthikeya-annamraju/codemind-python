s = 0
t = int(input())
vals = input()
lst = vals.split()
for i in range(len(lst)):
    if i %2 == 0:
        s = s + int(lst[i])
print(s)
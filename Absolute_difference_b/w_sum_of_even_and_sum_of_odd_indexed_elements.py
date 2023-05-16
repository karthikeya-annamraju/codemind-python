s = 0
s1 = 0
t = int(input())
vals = input()
lst = vals.split()
for i in range(len(lst)):
    #ODD
    if i %2 != 0:
        s = s + int(lst[i])
    #EVEN
    if i %2 == 0:
        s1 = s1 + int(lst[i])
print(s1 - s)
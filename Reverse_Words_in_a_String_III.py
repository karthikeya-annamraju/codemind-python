s = input()
lst = s.split()
for i in range(0, len(lst)):
    l = lst[i]
    n = "".join(reversed(l))
    print(n , end = " ")
s = 0
t = int(input())
vals = input()
lst = vals.split()
new_lst = []
for i in lst:
    new_lst.append(int(i))
    s = s + int(i)
print(max(new_lst))
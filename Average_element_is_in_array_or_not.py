s = 0
t = int(input())
vals = input()
lst = vals.split()
new_lst = []
for i in lst:
    new_lst.append(int(i))
    s = s + int(i)
avg = s//t
if avg in new_lst:
    print("True")
else :
    print("False")
t = int(input())
vals = input()
key = int(input())
lst = vals.split()
new_lst = []
for i in lst:
    new_lst.append(int(i))
if key in new_lst:
    print("True")
else :
    print("False")
s = input()
s2 = input()
x = s.lower()
y= s2.lower()
c = 0
a = x.split()
b = y.split()
for i in a:
    if i in b:
        c+=1
print(c)
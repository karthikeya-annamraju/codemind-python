s = 0
s1 = 0
t = int(input())
vals = input()
lst = vals.split()
for i in lst:
    if (int(i)%2!=0):
        s = s + int(i)
    if (int(i)%2==0):
        s1 = s1 + int(i)
x = s - s1
print(abs(x))
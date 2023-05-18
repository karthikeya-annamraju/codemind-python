s = input()
key = input()
count = 0
for i in range(0, len(s)):
    if s[i] == key:
        count+=1
if count == 0:
    print("-1")
else :
    print(count)
def is_Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True

x = int(input())
lst = []
for i in range(1, x+1):
    if x%i == 0:
        lst.append(i)
for val in lst:
    if is_Prime(val):
        lst.remove(val)
print(len(lst))
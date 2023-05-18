def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else :
        return True

a = int(input())
b = int(input())
for i in range(a, b+1):
    if (a == 1) :
        a+=1
    elif Prime(i):
        print(i)
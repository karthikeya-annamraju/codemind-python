def func(n):
    if '0' in str(n):
        pass
    else:
        x = n
        while (n!=0):
            rem = n % 10
            if x%rem == 0:
                n//=10
            else :
                break
        if (n == 0) :
            return True

a = int(input())
b = int(input())
for i in range(a, b+1):
    if func(i):
        print(i, end = " ")
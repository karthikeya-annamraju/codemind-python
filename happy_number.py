def Sums(n):
    s = 0
    while (n>0):
        rem = n % 10
        s = s + (rem*rem)
        n//=10
    if s < 9 and ( s == 1 or s == 7 ):
        print("True")
    elif s < 9 and (s != 1 or s!= 7):
        print("False")
    else :
        Sums(s)
    
num = int(input())
Sums(num)
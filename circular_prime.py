def Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True
    
def rev(n):
    rev = 0
    while n != 0:
        rev = (rev*10) + (n%10)
        n//=10
    return rev

num = int(input())
numrev = rev(num)
if Prime(num) and Prime(numrev):
    print("circular prime")
elif Prime(num) and Prime(numrev) == False:
    print("prime but not a circular prime")
else :
    print("not prime")
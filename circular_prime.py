def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    return True

def reverse(n):
    rev = 0
    while (n>0):
        rev = rev*10 + (n%10)
        n//=10
    return rev

num = int(input())
if is_prime(num) and is_prime(reverse(num)):
    print("circular prime")
elif is_prime(num):
    print("prime but not a circular prime")
else:
    print("not prime")

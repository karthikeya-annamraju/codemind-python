def is_Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True

def next_prime(t):
    count = 0
    for i in range(t+1, 10000):
        count+=1
        if is_Prime(i):
            break
    return count

a = int(input())
b = int(input())
check = a + b
res = next_prime(check)
print(res)
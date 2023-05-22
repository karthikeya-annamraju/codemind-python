def is_Prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
            break
    else:
        return True

def next_prime(t):
    cr = 0
    for i in range(t, 10000):
        #cr+=1
        if is_Prime(i):
            r_prime = i
            break
    return r_prime

def prev_prime(t):
    cl = 0
    for j in range(t-1, 1, -1):
        #cl+=1
        if is_Prime(j):
            l_prime = j
            break
    return l_prime

t = int(input())
for i in range(t):
    num = int(input())
    right = next_prime(num)
    left = prev_prime(num)    
    c = 0
    for k in range(num, right):
        c+=1
    c2 = 0
    for l in range(num, left, -1):
        c2+=1
    if abs(num-left) > abs(num - right):
        print(right)
    elif abs(num-left) < abs(num - right):
        print(left)
    else :
        print(left)
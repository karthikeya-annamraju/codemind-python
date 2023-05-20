def n_rev(n):
    rev = 0
    while n > 0:
        rev = (rev*10) + (n%10)
        n//=10
    return rev
    
num = int(input())
num_sq = num*num
rev_num = n_rev(num)
new = rev_num*rev_num
final = n_rev(new)
if(num_sq == final):
    print("True")
else :
    print("False")
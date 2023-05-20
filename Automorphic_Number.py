num = int(input())
n_sq = num*num
size = len(str(num))
res = n_sq%pow(10,size)  
if num == res:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
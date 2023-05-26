import math
n = int(input())
arr = list(map(int, input().split()))
print(math.gcd(*arr))
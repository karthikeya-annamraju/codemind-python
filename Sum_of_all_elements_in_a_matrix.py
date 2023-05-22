r, c = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(r)]
s = 0
s = sum([sum(j) for j in mat])
print(s)
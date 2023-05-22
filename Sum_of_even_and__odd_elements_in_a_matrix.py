r, c = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(r)]
odd_sum = 0
even_sum = 0
for i in mat :
    for j in i:
        if j % 2 == 0 :
            even_sum+=j
        else :
            odd_sum+=j
print(even_sum, odd_sum)
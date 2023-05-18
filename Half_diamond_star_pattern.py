def print_pattern(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end = "")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(i):
            print("*", end = "")
        print()

rows = int(input())
if (rows < 3):
    print("The pattern is not possible")
else :
    print_pattern(rows)
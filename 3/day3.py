with open("day3.txt", 'r') as f:
    data = f.readlines()

def day3(data, right, down):
    # slope: right 3, down 1
    width = len(data[0]) - 1
    x = 0
    y = 0
    trees = 0
    while y < len(data):
        if data[y][x] == "#":
            trees += 1
        y += down
        x = (x + right) % width
    return trees


print(day3(data, 3, 1))
l = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
out = 1
for angle in l:
    out *= day3(data, angle[0], angle[1])
print(out)
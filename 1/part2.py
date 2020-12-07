with open('day1.txt', 'r') as f:
    data = f.readlines()
    data = [int(i) for i in data]


def solve(data, sumTo):
    # assumes sorted data
    x = 0
    y = len(data) - 1
    while x < y:
        if (data[x] + data[y]) < sumTo:
            x += 1
        elif (data[x] + data[y]) > sumTo:
            y -= 1
        else:
            print(f"Sum to {sumTo}: {x}:{data[x]} + {y}:{data[y]} = {sumTo}")
            return data[x] * data[y]
    return False

def triplet(data, sumTo):
    data.sort()
    z = 0
    while z < len(data):
        temp = sumTo - data[z]
        if temp < 0:
            continue
        result = solve(data, temp)
        if result:
            return data[z] * result
        z += 1
    return False

print(triplet(data, 2020))
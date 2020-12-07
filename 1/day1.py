with open('day1.txt', 'r') as f:
    data = f.readlines()
    data = [int(i) for i in data]


def solve(data):
    data.sort()

    x = 0
    y = len(data) - 1
    while x < y:
        if (data[x] + data[y]) < 2020:
            x += 1
        elif (data[x] + data[y]) > 2020:
            y -= 1
        else:
            print(f"Sum to 2020: {x}:{data[x]} + {y}:{data[y]} = 2020")
            break
    return data[x] * data[y]

print(solve(data))
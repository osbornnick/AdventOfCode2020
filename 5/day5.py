with open("day5.txt", 'r') as f:
    data = f.readlines()

with open("test.txt", 'r') as f:
    test = f.readlines()

def process(data):
    ids = []
    for d in data:
        rowInfo = d[:7]
        colInfo = d[7:]
        row = process_binary(rowInfo, 0, 127)
        col = process_binary(colInfo, 0, 7)
        id = (row * 8) + col
        ids.append(id)
    return ids

    
def process_binary(info, low, high):
    for i in info:
        if (i == "F") or (i == "L"):
            high = (high + low) // 2
        if (i == "B") or (i == "R"):
            low = ((high + low) // 2) + 1
    return low


def get_seat_id(ids):
    possible = []
    for i in range(127):
        for j in range(7):
            possible.append((i * 8) + j)
    possible = [id for id in possible if id not in ids]
    for id in possible:
        if ((id + 1) in ids) and ((id - 1) in ids):
            print(id)
            
print(max(process(data)))
get_seat_id(process(data))
from collections import Counter

with open("day6.txt", 'r') as f:
    data = f.read()

def process(data):
    groups = data.split("\n\n")
    out = 0
    for group in groups:
        count = process_group(group)
        out += count
    return out


def process_group(group):
    out = 0
    answers = group.split()
    num = len(answers)
    c = Counter(''.join(answers))
    for count in c.keys():
        if c[count] == num:
            out += 1
    return out

print(process(data))
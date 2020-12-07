import parse
from collections import Counter

with open("day2.txt", 'r') as f:
    data = f.readlines()

def process(data):
    p = parse.compile("{min:d}-{max:d} {c}: {s}")
    parsed = []
    for d in data:
        parsed.append(p.parse(d))

    out = 0
    for result in parsed:
        count = Counter(result['s'])
        if count[result['c']] < result['min']:
            continue 
        if count[result['c']] > result['max']:
            continue
        out += 1
    return out

def part2(data):
    p = parse.compile("{first:d}-{second:d} {char}: {string}")
    parsed = []
    for d in data:
        parsed.append(p.parse(d))

    out = 0
    for result in parsed:
        s = result['string']
        c = result['char']
        first = result['first'] - 1
        second = result['second'] - 1
        if bool(s[first] == c) ^ bool(s[second] == c):
            out += 1
    return out


print(process(data))
print(part2(data))
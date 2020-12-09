with open("day9.txt", "r") as f:
    data = [int(line) for line in f.readlines()]


def p1(data, preamble_len):
    for i in range(preamble_len, len(data)):
        if not valid(i, data, preamble_len):
            return data[i]
    
    return None

    
def valid(i, data, preamble_len):
    preamble = data[i - preamble_len:i]
    preamble = list(set(preamble))
    preamble.sort()
    j = 0
    k = len(preamble) - 1
    while j < k:
        tempsum = preamble[j] + preamble[k]
        if tempsum == data[i]:
            return True
        elif tempsum < data[i]:
            j += 1
        elif tempsum > data[i]:
            k -= 1
    return False


def p2(data, preamble_len):
    sumTo = p1(data, preamble_len)
    i = 0
    j = 1
    while j < len(data):
        tempsum = sum(data[i:j])
        if tempsum == sumTo:
            return sumRule(data[i:j])
        elif tempsum < sumTo:
            j += 1
        else:
            i += 1
    
    return None


def sumRule(data):
    return min(data) + max(data)


if __name__ == "__main__":
    print(p1(data, 25))
    print(p2(data, 25))



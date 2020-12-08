import parse

with open("day8.txt", 'r') as f:
    data = f.readlines()

with open("test.txt", 'r') as f:
    test = f.readlines()


def process(data):
    boot = []
    p = parse.compile("{instr} {amt:d}")
    for d in data:
        parsed = p.parse(d)
        temp = {'instr': parsed['instr'], 'amt': parsed['amt'], 'run': False}
        boot.append(temp)
    return boot
    

def p1(boot):
    accumulator = 0
    i = 0
    while not boot[i]['run']:
        instr = boot[i]['instr']
        boot[i]['run'] = True
        if instr == 'acc':
            accumulator += boot[i]['amt']
            i += 1
        elif instr == 'jmp':
            i += boot[i]['amt']
        elif instr == 'nop':
            i += 1
    return accumulator


def p2(boot):
    for line in boot:
        changed = True
        prev = line['instr']
        if line['instr'] == 'jmp':
            line['instr'] = 'nop'
        elif line['instr'] == 'nop':
            line['instr'] == 'jmp'
        else:
            changed = False

        if changed:
            out = does_terminate(boot)
            if out[1]:
                return out[0]
            else:
                line['instr'] = prev


def does_terminate(boot):
    accumulator = 0
    i = 0
    j = 0
    # allow repeat instructions, but hard cap them
    while j < 1000:
        instr = boot[i]['instr']
        boot[i]['run'] = True
        if instr == 'acc':
            accumulator += boot[i]['amt']
            i += 1
        elif instr == 'jmp':
            i += boot[i]['amt']
        elif instr == 'nop':
            i += 1
        if i >= len(boot):
            return (accumulator, True)
        j += 1
    
    return (accumulator, False)

if __name__ == "__main__":
    print(p1(process(data)))
    print(p2(process(data)))

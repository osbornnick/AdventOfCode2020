import parse

with open("day7.txt", 'r') as f:
    data = f.readlines()

with open("test.txt", 'r') as f:
    test = f.readlines()

def process(data):
    p = parse.compile("{bag} bags contain {bag_string}")
    rules = {}
    for record in data:
        parsed = p.parse(record)
        rules[parsed['bag']] = parsed['bag_string']
    for rule in rules:
        r = rules[rule]
        sub_rules = []
        for bag_rule in parse.findall("{num:d} {bag} bag", r):
            d = {'num': bag_rule['num'], 'bag': bag_rule['bag']}
            sub_rules.append(d)
        rules[rule] = sub_rules
    return rules

def part1():
    rules = process(data)
    count = 0
    for bag in rules:
        if can_contain(bag, rules):
            count += 1
    print(count)


def part2(data):
    rules = process(data)
    print(count_all_bags("shiny gold", rules))


def can_contain(bag_name, rules):
    for rule in rules[bag_name]:
        if 'shiny gold' in rule['bag']:
            return True
        else:
            if can_contain(rule['bag'], rules):
                return True
    return False

def count_all_bags(bag_name, rules):
    # wrapper!
    return count_bags(bag_name, rules) - 1

def count_bags(bag_name, rules):
    # remember to minus one at the end
    count = 1
    for rule in rules[bag_name]:
        count += rule['num'] * count_bags(rule['bag'], rules)
    print(f"{bag_name} bags contains {count} bags")
    return count
    

part1()
part2(data)
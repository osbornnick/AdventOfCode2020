with open("day4.txt", 'r') as f:
    data = f.read()

def process(data):
    passports = data.split('\n\n')
    numValid = 0
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for p in passports:
        valid = True
        for f in fields:
            if f not in p:
                valid = False
                break
        if valid and validate(p):
            numValid += 1
    return numValid

def validate(passport):
    data = passport.split()
    for d in data:
        if d[:3] == "byr":
            if not valid_byr(d[4:]):
                return False 
        if d[:3] == "iyr":
            if not valid_iyr(d[4:]):
                return False 
        if d[:3] == "eyr":
            if not valid_eyr(d[4:]):
                return False 
        if d[:3] == "hgt":
            if not valid_hgt(d[4:]):
                return False 
        if d[:3] == "hcl":
            if not valid_hcl(d[4:]):
                return False 
        if d[:3] == "ecl":
            if not valid_ecl(d[4:]):
                return False 
        if d[:3] == "pid":
            if not valid_pid(d[4:]):
                return False
    return True

def valid_byr(byr):
    if len(byr) != 4:
        return False
    if (int(byr) < 1920) or (int(byr) > 2002):
        return False
    return True

def valid_iyr(iyr):
    if len(iyr) != 4:
       return False
    if (int(iyr) < 2010) or (int(iyr) > 2020):
        return False
    return True

def valid_eyr(eyr):
    if len(eyr) != 4:
       return False
    if (int(eyr) < 2020) or (int(eyr) > 2030):
        return False
    return True

def valid_hgt(hgt):
    if len(hgt) < 3:
        return False

    height = int(hgt[:-2])
    if hgt[-2:] == "cm":
        if (height < 150) or (height > 193):
            return False
    elif hgt[-2:] == "in":
        if (height < 59) or (height > 76):
            return False
    else:
        return False
    return True

def valid_hcl(hcl):
    if hcl[0] != "#":
        return False
    for c in hcl[1:]:
        if c not in "0123456789abcdef":
            return False
    return True

def valid_ecl(ecl):
    if ecl not in "amb blu brn gry grn hzl oth":
        return False
    return True

def valid_pid(pid):
    if len(pid) != 9:
        return False
    return True

print(process(data))
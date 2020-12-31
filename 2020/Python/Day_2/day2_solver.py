def get_min_chars(str):
    hyphen = str.find('-')
    if hyphen == 2:
        return int(str[0:2])
    else:
        return int(str[0])


def get_max_chars(str):
    hyphen = str.find('-')
    space = str.find(' ')
    if space - hyphen == 3:
        return int(str[hyphen + 1 : space])
    else:
        return int(str[hyphen + 1])


f = open('input_file_pwd.txt', 'r').readlines()


def part_1(f):
    valid_passwords = 0
    for line in f:
        char = line[line.find(':') - 1]
        min_chars_allowed = get_min_chars(line)
        max_chars_allowed = get_max_chars(line)
        pwd = line[line.find(':') + 2: ]
        count_char = pwd.count(char)
        if count_char <= max_chars_allowed and count_char >= min_chars_allowed:
            valid_passwords += 1
    return valid_passwords


def part_2(f):
    valid_pwds = 0
    for line in f:
        char = line[line.find(':') - 1]
        min_chars_allowed = get_min_chars(line)
        max_chars_allowed = get_max_chars(line)
        pwd = line[line.find(':') + 2:]
        if pwd[min_chars_allowed - 1] == char and pwd[max_chars_allowed - 1] != char:
            valid_pwds += 1
        elif pwd[min_chars_allowed - 1] != char and pwd[max_chars_allowed - 1] == char:
            valid_pwds += 1
    return valid_pwds

def tests():
    print(part_1(f))
    assert part_1(f) == 447, "There is 447 valid lines in part 1"

    print(part_2(f))
    assert part_2(f) == 249, "There is 249 valid lines in part 2"

tests()

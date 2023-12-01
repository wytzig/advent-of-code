import re


def solve_line(line):
    number = ""
    for character in line:
        if number == "":
            if character.isnumeric():
                number = number + character
    matches = re.finditer(r'\d', line)

    last_digit = None
    for match in matches:
        last_digit = match.group()

    number = number + last_digit
    return number


def solve_part1(input):
    result = 0
    for line in input.splitlines():
        result = result + int(solve_line(line))
    return result


def solve_part2(input):
    result = 0
    for line in input.splitlines():
        number_to_add = int(solve_line(line))
        result = result + number_to_add
    return result


def solve_part3(input):
    return "answer of puzzle 3"


def solve_part4(input):
    return "answer of puzzle 4"

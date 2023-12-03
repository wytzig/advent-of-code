import re

DIGIT_MAPPING: dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_and_last_digits(digits):
    all_digits = "".join([DIGIT_MAPPING.get(digit, digit) for digit in digits])
    return int(all_digits[0] + all_digits[-1])


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


def solve_first(document_input):
    result = 0
    for line in document_input.splitlines():
        number_to_add = int(solve_line(line))
        result = result + number_to_add
    return result


def solve_second(document_input):
    result = 0
    for line in document_input.splitlines():
        digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d+))", line)
        result = result + get_first_and_last_digits(digits)
    return result


def solve_part1(document_input):
    return solve_first(document_input)


def solve_part2(document_input):
    return solve_first(document_input)


def solve_part3(document_input):
    return solve_second(document_input)


def solve_part4(document_input):
    return solve_second(document_input)

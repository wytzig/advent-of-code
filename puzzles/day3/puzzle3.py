def has_special_character(s):
    special_characters = " !\"#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"
    if any(c in special_characters for c in s):
        return True
    else:
        return False


def is_valid_position(i, j, rows, cols):
    return 0 <= i < rows and 0 <= j < cols


def get_surrounding_values(i, j, data):
    rows = len(data)
    cols = len(data[0])
    surrounding_values = []

    # Relative positions for the eight surrounding positions
    relative_positions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for dx, dy in relative_positions:
        new_i, new_j = i + dx, j + dy
        if is_valid_position(new_i, new_j, rows, cols):
            value = data[new_i][new_j]

            # If the character is numeric, find the whole number
            if value.isnumeric():
                start_i, start_j = new_i, new_j

                # Find the start of the number in the row
                while start_j > 0 and data[start_i][start_j - 1].isnumeric():
                    start_j -= 1

                # Collect the whole number
                number = ''.join(char for char in data[start_i][start_j:new_j + 1] if char.isnumeric())
                if number not in surrounding_values:
                    surrounding_values.append(number)
            elif value != '.':
                # Exclude '.' from the response
                surrounding_values.append(value)

    return surrounding_values


def solve_part1(document_input):
    data = document_input.splitlines()
    for i in range(len(data)):
        print(data[i])
        for j in range(len(data[i])):
            list_of_surrounding_values = []
            if has_special_character(data[i][j]):
                list_of_surrounding_values = get_surrounding_values(i, j, data)
            print("test test ")




    return "test"


def solve_part2(document_input):
    return "test"


def solve_part3(document_input):
    return "test"


def solve_part4(document_input):
    return "test"

def get_number_from_text(text_input):
    result = ""
    for character in text_input:
        if character.isnumeric():
            result += character
        elif result:
            break
    return int(result)


def get_text_without_number_from_text(text_input):
    result = ""
    for character in text_input:
        if not character.isnumeric():
            result = result + character
    return result.strip()


def solve_games(document_input, to_match_against):
    list_of_games = str.splitlines(document_input)
    result = 0

    # game is defined as "metadata:game_data" i.e. "game 1: set1; set2; set3"
    for game in list_of_games:
        game_packet = str.split(game, ":")
        game_metadata = game_packet[0]
        game_data = game_packet[1]
        is_invalid_game = False
        for game_set in str.split(game_data, ";"):
            colored_cubes = str.split(game_set, ",")
            for chosen_set_colored_cube in colored_cubes:
                get_number_from_text(chosen_set_colored_cube)

                for chosen_match_cube in str.split(to_match_against, ","):
                    if get_text_without_number_from_text(chosen_set_colored_cube) in get_text_without_number_from_text(
                            chosen_match_cube):
                        if get_number_from_text(chosen_set_colored_cube) > get_number_from_text(chosen_match_cube):
                            is_invalid_game = True
                            break
                        else:
                            continue
            if is_invalid_game:
                break
        if not is_invalid_game:
            result += get_number_from_text(game_metadata)
    return result


def check_color_existing_in_predefined_list(entry, color_set):
    for color in color_set:
        if get_text_without_number_from_text(color) in get_text_without_number_from_text(entry):
            return True
    return False


def is_new_entry_bigger(entry, color_set):
    for color in color_set:
        if get_text_without_number_from_text(color) in get_text_without_number_from_text(entry):
            if get_number_from_text(entry) > get_number_from_text(color):
                return True
            else:
                return False
    return False


def update_entry_in_list(initial_list, entry_to_add):
    new_list = []
    for entry in initial_list:
        if get_text_without_number_from_text(entry) == get_text_without_number_from_text(entry_to_add):
            new_list.append(entry_to_add)
        else:
            new_list.append(entry)
    return new_list


def solve_powers(document_input):
    list_of_games = str.splitlines(document_input)
    game_power_sum = 0

    for game in list_of_games:
        game_packet = str.split(game, ":")
        game_data = game_packet[1]
        all_color_sets = []
        for game_set in str.split(game_data, ";"):
            for colored_cube in str.split(game_set, ","):
                if not check_color_existing_in_predefined_list(colored_cube, all_color_sets):
                    all_color_sets.append(colored_cube)
                elif is_new_entry_bigger(colored_cube, all_color_sets):
                    all_color_sets = update_entry_in_list(all_color_sets, colored_cube)
        game_power = 0
        for color_set in all_color_sets:
            if game_power == 0:
                game_power = get_number_from_text(color_set)
            else:
                game_power *= get_number_from_text(color_set)
        game_power_sum += game_power
    return game_power_sum


def solve_part1(document_input):
    return solve_games(document_input, "12 red, 13 green, 14 blue")


def solve_part2(document_input):
    return solve_games(document_input, "12 red, 13 green, 14 blue")


def solve_part3(document_input):
    return solve_powers(document_input)


def solve_part4(document_input):
    return solve_powers(document_input)

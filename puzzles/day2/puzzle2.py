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
                    if get_text_without_number_from_text(chosen_set_colored_cube) in get_text_without_number_from_text(chosen_match_cube):
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


def solve_part1(document_input):
    return solve_games(document_input, "12 red, 13 green, 14 blue")


def solve_part2(document_input):
    return solve_games(document_input, "12 red, 13 green, 14 blue")


def solve_part3(document_input):
    return "test"


def solve_part4(document_input):
    return "test"

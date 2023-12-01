import time
from puzzles import puzzle1  # Import your puzzle modules


def execute_puzzle(puzzle_module, input_file, input_file2, input_file3, input_file4):
    with open(input_file, 'r') as file:
        input_data = file.read()
    with open(input_file2, 'r') as file:
        input_data2 = file.read()
    with open(input_file3, 'r') as file:
        input_data3 = file.read()
    with open(input_file4, 'r') as file:
        input_data4 = file.read()

    start_time = time.time()
    answer_part1 = puzzle_module.solve_part1(input_data)
    elapsed_time_part1 = int((time.time() - start_time) * 1000)

    start_time = time.time()
    answer_part2 = puzzle_module.solve_part2(input_data2)
    elapsed_time_part2 = int((time.time() - start_time) * 1000)

    start_time = time.time()
    answer_part3 = puzzle_module.solve_part3(input_data3)
    elapsed_time_part3 = int((time.time() - start_time) * 1000)

    start_time = time.time()
    answer_part4 = puzzle_module.solve_part4(input_data4)
    elapsed_time_part4 = int((time.time() - start_time) * 1000)

    return answer_part1, elapsed_time_part1, answer_part2, elapsed_time_part2, answer_part3, elapsed_time_part3, answer_part4, elapsed_time_part4


if __name__ == "__main__":
    input_file_puzzle1 = "puzzles/input_puzzle1-1.txt"
    input_file_puzzle2 = "puzzles/input_puzzle1-2.txt"
    input_file_puzzle3 = "puzzles/input_puzzle1-3.txt"

    answer1, time1, answer2, time2, answer3, time3, answer4, time4 = execute_puzzle(puzzle1, input_file_puzzle1, input_file_puzzle2, input_file_puzzle3, input_file_puzzle2)
    print(f"Day 1, Puzzle 1:\n\tAnswer Part 1: {answer1} [{time1}ms]\n\tAnswer Part 2: {answer2} [{time2}ms]\n\tAnswer Part 3: {answer3} [{time3}ms]\n\tAnswer Part 4: {answer4} [{time4}ms]")

def calculate_unmarked(lottery_numbers, board):
    diff = []
    for row in board:
        row_diff = list(set(row) - set(lottery_numbers))
        for d in row_diff:
            diff.append(d)

    return sum(diff)

def play_first_win(numbers_set, boards):
    for board in boards:
        for row in board:
            if set(row).issubset(set(numbers_set)):
                return calculate_unmarked(numbers_set, board) * numbers_set[-1]

    return None


def first_win(lottery_numbers, boards):
    initial = 5
    bid = 0
    while True:
        bid += 1

        if result := play_first_win(lottery_numbers[0:initial + bid], boards):
            print('Winner!: ', result)
            break

        if initial_offset + bid >= len(lottery_numbers):
            raise Exception('Finish lottery by force!')


def play(numbers, boards):
    for board_index, board in enumerate(boards):
        for row in board:
            if set(row).issubset(set(numbers)):
                boards.pop(board_index)
                continue

    return boards


def last_win(numbers, boards):


    bid = 0
    initial_number = 5
    while True:
        boards = play(numbers[0:initial_number+bid], boards)
        print(boards)

        if len(boards) < 2:
            unmarked_sum = calculate_unmarked(numbers[0:initial_number + bid], boards[0])
            print(unmarked_sum)
            print(numbers[initial_number + bid])

            correct_sum = unmarked_sum - numbers[initial_number + bid]
            print('Last win:', correct_sum * numbers[initial_number + bid])

            break

        bid += 1


with open('input.txt') as f:
    data = f.read().split('\n')

    numbers = [int(n) for n in data[0].split(',')]

    bingo_boards = data[1:]


    bingo_boards = [board for board in bingo_boards if board != '']

    chunks = [bingo_boards[i:i + 5] for i in range(0, len(bingo_boards), 5)]

    parsed_rows = []
    for chunk in chunks:
        new_board = []
        for row in chunk:
            new_board.append([int(r) for r in row.split(' ') if r != ''])
        parsed_rows.append(new_board)


    initial_offset = 5
    # filter empty lines
    numbers_play_set = numbers[0:initial_offset]

    # first_win(numbers, parsed_rows)
    #
    # print(parsed_rows)

    last_win(numbers, parsed_rows)






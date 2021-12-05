def calculate_unmarked(lottery_numbers, board):
    diff = []
    for row in board:
        row_diff = list(set(row) - set(lottery_numbers))
        for d in row_diff:
            diff.append(d)

    return sum(diff)


win_number_set = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24]
unmarked_board = [
    [14, 21, 17, 24, 4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7]
]

assert 188 == calculate_unmarked(win_number_set, unmarked_board)


def play(numbers_set, boards):
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

        if result := play(lottery_numbers[0:initial + bid], boards):
            print('Winner!: ', result)
            break

        if initial_offset + bid >= len(lottery_numbers):
            raise Exception('Finish lottery by force!')



with open('input.txt') as f:
    data = f.read().split('\n')

    numbers = [int(n) for n in data[0].split(',')]

    bingo_boards = data[1:]

    parsed = [board for i, board in enumerate(bingo_boards) if board != '']

    chunks = [parsed[i:i + 5] for i in range(0, len(bingo_boards), 5)]

    parsed_rows = []
    for chunk in chunks:
        new_board = []
        for row in chunk:
            new_board.append([int(r) for r in row.split(' ') if r != ''])
        parsed_rows.append(new_board)

    initial_offset = 5
    # filter empty lines
    numbers_play_set = numbers[0:initial_offset]

    first_win(numbers, parsed_rows)


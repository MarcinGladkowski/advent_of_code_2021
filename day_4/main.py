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
    diff = []
    won = False
    print("Start lotterry!")
    for board in boards:

        print(board)

        for row in board:
            # diff of numbers from row and lottery
            row = [int(r) for r in row.split(' ') if r != '']  # parsing each row
            print(row)

            row_diff = list(set(row) - set(numbers_set))
            for d in row_diff:
                diff.append(d)

            if set(row).issubset(set(numbers_set)):
                won = True



    print(sum(diff))
    print(diff)

    return won


with open('test_input.txt') as f:
    data = f.read().split('\n')

    numbers = [int(n) for n in data[0].split(',')]

    bingo_boards = data[1:]

    parsed = [board for i, board in enumerate(bingo_boards) if board != '']
    chunks = [parsed[i:i + 5] for i in range(0, len(bingo_boards), 5) if bingo_boards != '']

    initial_offset = 5
    # filter empty lines
    numbers_play_set = numbers[0:initial_offset]

    bid = 0
    while True:
        bid += 1

        if play(numbers[0:initial_offset + bid], chunks):
            print('Winner!')
            break

        if initial_offset + bid >= len(numbers):
            raise print('Finish lottery!')

def calculate_win(lottery_numbers, bingo_board):
    pass

def play(numbers_set, boards):
    for board in boards:
        if board != '':
            rows = board.split('\n')

            for row in rows:
                row = [int(r) for r in row.split(' ') if r != '']
                if set(row).issubset(set(numbers_set)):
                    print('The winner set is ', row)
                    # get last win number and get sum of unmarked
                    return True
    return False


with open('test_input.txt') as f:
    data = f.read().split('\n')

    numbers = [int(n) for n in data[0].split(',')]

    bingo_boards = data[1:]

    parsed = [board for i, board in enumerate(bingo_boards) if board != '']
    chunks = [parsed[i:i+5] for i in range(0, len(bingo_boards), 5) if bingo_boards != '']

    initial_offset = 5
    # filter empty lines
    numbers_play_set = numbers[0:initial_offset]

    bid = 0
    while True:
        bid += 1

        if play(numbers[0:initial_offset+bid], bingo_boards):
            print('Winner!')
            break

        if initial_offset+bid >= len(numbers):
            raise print('Finish lottery!')

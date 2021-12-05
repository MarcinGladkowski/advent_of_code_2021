def play(numbers_set, boards):
    for board in boards:
        if board != '':
            rows = board.split('\n')

            for row in rows:
                row = [int(r) for r in row.split(' ') if r != '']

                print(row, numbers_set)

                if set(row).issubset(set(numbers_set)):
                    print('The winner set is ', row)

                    return True
    return False


with open('test_input.txt') as f:
    data = f.read().split('\n')

    numbers = [int(n) for n in data[0].split(',')]

    bingo_boards = data[1:]
    initial_offset = 5
    # filter empty lines
    numbers_play_set = numbers[0:initial_offset]

    index = 0
    while True:
        index += 1

        if play(numbers[0:initial_offset+index], bingo_boards):
            print('Winner!')
            break

        if initial_offset+index >= len(numbers):
            raise print('Finish lottery!')

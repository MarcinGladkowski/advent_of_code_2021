with open('test_input.txt') as f:
    data = f.read().split('\n')

    numbers = data[0]

    bingo_boards = data[1:]
    # filter empty lines


    for bingo in bingo_boards:
        if bingo != '':
            rows = bingo.split('\n')

            for row in rows:
                print(row)


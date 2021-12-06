numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

boards = [
    [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ], [
        [3, 15, 0, 2, 22],
        [9, 18, 13, 17, 5],
        [19, 8, 7, 25, 23],
        [20, 11, 10, 24, 4],
        [14, 21, 16, 12, 6]
    ],
    [
        [14, 21, 17, 24, 4],
        [10, 16, 15, 9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7]
    ]
]

def play(numbers, boards):
    for board_index, board in enumerate(boards):
        for row in board:
            if set(row).issubset(set(numbers)):
                boards.pop(board_index)
                continue

    return boards

bid = 0
initial_number = 5

def calculate_unmarked(lottery_numbers, board):
    diff = []
    for row in board:
        row_diff = list(set(row) - set(lottery_numbers))
        print(row_diff)
        for d in row_diff:
            diff.append(d)

    return sum(diff)



while True:
    boards = play(numbers[0:initial_number+bid], boards)

    if len(boards) < 2:
        unmarked_sum = calculate_unmarked(numbers[0:initial_number + bid], boards[0])
        correct_sum = unmarked_sum - numbers[initial_number + bid]
        print(correct_sum * numbers[initial_number + bid])

        break

    bid += 1



import re

with open('input.txt') as f:
    data = f.read().split('\n')
    moves = {
        'forward': 0,
        'up': 0,
        'down': 0
    }
    for dict_move in moves.items():
        compiled = re.compile(f'{dict_move[0]}\s\d')
        for move in re.findall(compiled, ','.join(data)):
            moves[dict_move[0]] += int(re.sub(r'\w+', '', move, 1))

    print(int(moves['forward']) * (int(moves['down']) - int(moves['up'])))
with open('test_input_1.txt') as f:
    split_data = f.read().split('\n')


def parse_point(point: str):
    split = point.split(',')

    return {
        'x': int(split[0]),
        'y': int(split[1])
    }


assert {'x': 0, 'y': 9} == parse_point('0,9')


def parse_input(data):
    pass

# def parse_line(line):


# assert { 'start': { 'x': 0, 'y': 9 }, 'end': {'x': 5, 'y': 9 }} == parse_line(['0'])

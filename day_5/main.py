with open('test_input_1.txt') as f:
    split_data = f.read().split('\n')


def parse_point(point: str):
    split = point.split(',')

    return {
        'x': int(split[0]),
        'y': int(split[1])
    }


assert {'x': 0, 'y': 9} == parse_point('0,9')


def parse_line(line):
    split = line.split('->')

    return {
        'start': parse_point(split[0].strip()),
        'end': parse_point(split[1].strip()),
    }


assert {'start': {'x': 0, 'y': 9}, 'end': {'x': 5, 'y': 9}} == parse_line('0,9 -> 5,9')

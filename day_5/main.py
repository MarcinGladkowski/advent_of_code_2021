with open('test_input_1.txt') as f:
    split_data = f.read().split('\n')
    # print(split_data)


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


def parse_points(data: list):
    return [parse_line(line_data) for line_data in data]


assert [{'start': {'x': 0, 'y': 9}, 'end': {'x': 5, 'y': 9}},
        {'start': {'x': 0, 'y': 9}, 'end': {'x': 2, 'y': 9}}] == parse_points(['0,9 -> 5,9', '0,9 -> 2,9'])


def filter_not_straight(coords):
    return coords.get('start').get('x') == coords.get('end').get('x') or coords.get('start').get('y') == coords.get(
        'end').get('y')


assert True is filter_not_straight({'start': {'x': 0, 'y': 9}, 'end': {'x': 5, 'y': 9}})
assert False is filter_not_straight({'start': {'x': 1, 'y': 9}, 'end': {'x': 5, 'y': 3}})


def parse_data(data):
    return [point for point in parse_points(data) if filter_not_straight(point)]


assert [{'start': {'x': 0, 'y': 9}, 'end': {'x': 5, 'y': 9}}] == parse_data(['0,9 -> 5,9', '8,0 -> 0,8'])


def draw_map(points):
    """
    Get highest x and y
    Draw map from parsed point
    """
    x_start = [x.get('start').get('x') for x in points]
    x_end = [x.get('end').get('x') for x in points]

    y_start = [x.get('start').get('y') for x in points]
    y_end = [x.get('end').get('y') for x in points]

    print(x_start, x_end)

    pass


draw_map([
    {'start': {'x': 0, 'y': 9}, 'end': {'x': 5, 'y': 9}},
    {'start': {'x': 0, 'y': 9}, 'end': {'x': 2, 'y': 9}}
])

def power_consumption(binary_numbers):
    oxygen_generator_rating = 0

    storage = {}
    for binary in binary_numbers:
        for index, bit in enumerate(binary):

            if storage.get(index) is None:
                storage[index] = {
                    '0': 0,
                    '1': 0
                }

            if storage[index].get(bit, 0):
                storage[index][bit] += 1
            else:
                storage[index][bit] = 1

    most_commons = []
    less_commons = []
    for bits in storage.values():
        most_commons.append('0' if int(bits['0']) > int(bits['1']) else '1')
        less_commons.append('1' if int(bits['0']) > int(bits['1']) else '0')

    return int(''.join(most_commons), 2) * int(''.join(less_commons), 2), oxygen_generator_rating


with open('test_input.txt') as f:
    data = f.read().split('\n')
    assert 198 == power_consumption(data)[0]
    assert '10111' == power_consumption(data)[1]

with open('input.txt') as f:
    data = f.read().split('\n')
    assert 1131506 == power_consumption(data)[0]

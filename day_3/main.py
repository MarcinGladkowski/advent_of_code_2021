def power_consumption(binary_numbers):
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

    return int(''.join(most_commons), 2) * int(''.join(less_commons), 2)


def zero_lead(zero, one):
    return '0' if zero > one else '1'

def one_lead(zero, one):
    return '0' if zero < one else '1'

def oxygen_generator_rating(binary_numbers, startIndex, number_strategy):

    if startIndex > 999:
        raise Exception('Infinitive loop Marcin!')


    if len(binary_numbers) == 1:
        return int(binary_numbers[0], 2)

    zero = 0
    one = 0
    for binary in binary_numbers:

        if binary[startIndex] == '0':
            zero += 1
        if binary[startIndex] == '1':
            one += 1


    binary_numbers = [number for number in binary_numbers if number[startIndex] == number_strategy(zero, one)]

    return oxygen_generator_rating(binary_numbers, startIndex+1, number_strategy)


with open('test_input.txt') as f:
    data = f.read().split('\n')
    assert 198 == power_consumption(data)
    assert 23 == oxygen_generator_rating(data, 0, zero_lead)

with open('input.txt') as f:
    data = f.read().split('\n')
    assert 1131506 == power_consumption(data)

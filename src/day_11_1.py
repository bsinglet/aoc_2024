#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '15 December 2024'
__version__ = '0.1.0'


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = [int(x) for x in my_lines.split(' ')]
    return my_lines


def calculate_stones(my_lines: list) -> int:
    stones = my_lines
    for turns_simulated in range(25):
        # print(f"After {turns_simulated} blinks, the stones are {stones}")
        new_stones = list()
        for each_stone in stones:
            if each_stone == 0:
                new_stones.append(1)
            elif len(str(each_stone)) % 2 == 0:
                each_stone = str(each_stone)
                new_stones.append(int(each_stone[:int(len(each_stone)/2)]))
                new_stones.append(int(each_stone[int(len(each_stone)/2):]))
            else:
                new_stones.append(each_stone * 2024)
        stones = new_stones
    return len(stones)


def main():
    filename = '..\\inputs\\day11.txt'
    my_lines = load_input(filename=filename)
    result_0 = calculate_stones(my_lines)
    print(f'There are {result_0} stones after blinking 25 times.')


if __name__ == '__main__':
    main()

#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '12 December 2024'
__version__ = '0.1.0'

import unittest


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split('\n')
    return my_lines


def get_all_permutations(nodes: list) -> list:
    permutations = list()
    for index in range(len(nodes)-1):
        for index_2 in range(index+1, len(nodes)):
            permutations.append((nodes[index], nodes[index_2]))
    return permutations


def get_antinodes(position_0: tuple, position_1: tuple, map_x: int, map_y: int) -> list:
    antinodes = list()
    candidates = list()
    d_x = position_1[0] - position_0[0]
    d_y = position_1[1] - position_0[1]
    candidates.append((position_0[0] - d_x, position_0[1] - d_y))
    candidates.append((position_1[0] + d_x, position_1[1] + d_y))
    for each_candidate in candidates:
        if each_candidate[0] >= 0 and each_candidate[0] < map_x:
            if each_candidate[1] >= 0 and each_candidate[1] < map_y:
                antinodes.append(each_candidate)
    return antinodes


def get_antinodes_2(position_0: tuple, position_1: tuple, map_x: int, map_y: int) -> list:
    antinodes = list()
    d_x = position_1[0] - position_0[0]
    d_y = position_1[1] - position_0[1]
    temp_candidate = position_0
    while True:
        temp_candidate = (temp_candidate[0] - d_x, temp_candidate[1] - d_y)
        if temp_candidate[0] < 0 or temp_candidate[0] >= map_x:
            break
        if temp_candidate[1] < 0 or temp_candidate[1] >= map_y:
            break
        antinodes.append(temp_candidate)
    temp_candidate = position_1
    while True:
        temp_candidate = (temp_candidate[0] + d_x, temp_candidate[1] + d_y)
        if temp_candidate[0] < 0 or temp_candidate[0] >= map_x:
            break
        if temp_candidate[1] < 0 or temp_candidate[1] >= map_y:
            break
        antinodes.append(temp_candidate)
    return antinodes


def find_unique_antinodes(my_lines: list) -> int:
    antinodes = dict()
    antennas = dict()
    frequencies = list(set([x for x in ''.join(my_lines).replace('.', '')]))
    for each_frequency in frequencies:
        antennas[each_frequency] = list()
    for y_index in range(len(my_lines)):
        for x_index in range(len(my_lines[y_index])):
            if my_lines[y_index][x_index] != '.':
                antennas[my_lines[y_index][x_index]].append((x_index, y_index))
    for each_frequency in frequencies:
        for each_pair_of_nodes in get_all_permutations(antennas[each_frequency]):
            found_antinodes = get_antinodes(each_pair_of_nodes[0], each_pair_of_nodes[1], len(my_lines[0]), len(my_lines))
            for each_antinode in found_antinodes:
                # print(f"Found {each_antinode} with {each_pair_of_nodes} from {each_frequency}")
                antinodes[(each_antinode[0], each_antinode[1])] = '#'
    # draw the output for debugging
    for y in range(len(my_lines)):
        my_lines[y] = [z for z in my_lines[y]]
    for each_antinode in antinodes.keys():
        my_lines[each_antinode[1]][each_antinode[0]] = '#'
    """for each_row in my_lines:
        print(''.join(each_row))
    # print(antinodes)"""
    return len(antinodes.keys())


def find_unique_antinodes_2(my_lines: list) -> int:
    antinodes = dict()
    antennas = dict()
    frequencies = list(set([x for x in ''.join(my_lines).replace('.', '')]))
    for each_frequency in frequencies:
        antennas[each_frequency] = list()
    for y_index in range(len(my_lines)):
        for x_index in range(len(my_lines[y_index])):
            if my_lines[y_index][x_index] != '.':
                antennas[my_lines[y_index][x_index]].append((x_index, y_index))
    for each_frequency in frequencies:
        for each_pair_of_nodes in get_all_permutations(antennas[each_frequency]):
            found_antinodes = get_antinodes_2(each_pair_of_nodes[0], each_pair_of_nodes[1], len(my_lines[0]), len(my_lines))
            for each_antinode in found_antinodes:
                # print(f"Found {each_antinode} with {each_pair_of_nodes} from {each_frequency}")
                antinodes[(each_antinode[0], each_antinode[1])] = '#'
    for y in range(len(my_lines)):
        my_lines[y] = [z for z in my_lines[y]]
    # every antenna is automatically an antinode now
    for each_frequency in frequencies:
        for each_antenna in antennas[each_frequency]:
            antinodes[(each_antenna[0], each_antenna[1])] = '#'
    # mark all the antinodes on the map for debugging
    for each_antinode in antinodes.keys():
        my_lines[each_antinode[1]][each_antinode[0]] = '#'
    # draw the output for debugging
    """for each_row in my_lines:
        print(''.join(each_row))"""
    # print(antinodes)
    return len(antinodes.keys())


def main():
    filename = '..\\inputs\\day08.txt'
    my_lines = load_input(filename=filename)
    result_0 = find_unique_antinodes(my_lines)
    print(f'There are {result_0} unique locations within the bounds of the map that contain an antinode.')
    my_lines = load_input(filename=filename)
    result_1 = find_unique_antinodes_2(my_lines)
    print(f'There are {result_1} unique locations within the bounds of the map that contain an antinode.')


if __name__ == '__main__':
    main()

class TestDay08Methods(unittest.TestCase):
    def test_get_antinodes_01(self):
        self.assertEqual(get_antinodes((8, 8), (9, 9), 12, 12), [(7, 7), (10, 10)])

    def test_get_antinodes_02(self):
        self.assertEqual(get_antinodes((4, 5), (4, 8), 12, 12), [(4, 2), (4, 11)])
    
    def test_get_antinodes_03(self):
        self.assertEqual(get_antinodes((8, 1), (5, 2), 12, 12), [(11, 0), (2, 3)])
    
    def test_get_antinodes_2_01(self):
        self.assertEqual(get_antinodes_2((8, 8), (9, 9), 12, 12), [])
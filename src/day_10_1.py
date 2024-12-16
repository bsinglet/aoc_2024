#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '15 December 2024'
__version__ = '0.1.0'

import unittest


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split('\n')
    for index in range(len(my_lines)):
        my_lines[index] = [int(x) for x in my_lines[index]]
    return my_lines


def get_trailheads_and_peaks(my_lines: list) -> tuple:
    all_peaks = list()
    all_trailheads = list()
    for y in range(len(my_lines)):
        for x in range(len(my_lines[y])):
            if my_lines[y][x] == 0:
                all_trailheads.append((x, y))
            elif my_lines[y][x] == 9:
                all_peaks.append((x, y))
    return (all_peaks, all_trailheads)


def get_neighbors(my_lines: list, each_trailhead: tuple, map_x: int, map_y: int) -> list:
    neighbors = list()
    candidates = [(each_trailhead[0]-1, each_trailhead[1]), 
                  (each_trailhead[0]+1, each_trailhead[1]), 
                  (each_trailhead[0], each_trailhead[1]-1), 
                  (each_trailhead[0], each_trailhead[1]+1)]
    for each_candidate in candidates:
        # print(f"Checking candidate ({each_candidate[0]}, {each_candidate[1]})")
        if each_candidate[0] >=0 and each_candidate[0] < map_x:
            if each_candidate[1] >= 0 and each_candidate[1] < map_y:
                # print(f"Comparing height {my_lines[each_trailhead[1]][each_trailhead[0]]} to {my_lines[each_candidate[1]][each_candidate[0]]}")
                if my_lines[each_trailhead[1]][each_trailhead[0]] + 1 == my_lines[each_candidate[1]][each_candidate[0]]:
                    neighbors.append(each_candidate)
    return neighbors


def calculate_trailhead_scores(my_lines: list) -> int:
    trailhead_sum = 0
    peaks, trailheads = get_trailheads_and_peaks(my_lines)
    for each_trailhead in trailheads:
        # print(f"Using trailhead ({each_trailhead[0], each_trailhead[1]})")
        visited = {each_trailhead: True}
        pending = list()
        neighbors = get_neighbors(my_lines, each_trailhead, len(my_lines), len(my_lines[0]))
        for each_neighbor in neighbors:
            if each_neighbor not in visited and each_neighbor not in pending:
                # print(f"Adding neighbor ({each_neighbor[0], each_neighbor[1]}) to pending")
                pending.append(each_neighbor)
        while len(pending) > 0:
            current_location = pending.pop()
            # print(f"Getting neighbors of ({current_location[0]}, {current_location[1]})")
            visited[current_location] = True
            neighbors = get_neighbors(my_lines, current_location, len(my_lines), len(my_lines[0]))
            for each_neighbor in neighbors:
                if each_neighbor not in visited:
                    pending.append(each_neighbor)
            if my_lines[current_location[1]][current_location[0]] == 9:
                trailhead_sum += 1
    return trailhead_sum


def main():
    filename = '..\\inputs\\day10.txt'
    my_lines = load_input(filename=filename)
    result_0 = calculate_trailhead_scores(my_lines)
    print(f'The sum of the scores of all trailheads on my tropographic map is {result_0}.')


if __name__ == '__main__':
    main()


class TestDay10Methods(unittest.TestCase):
    def test_calculate_trailhead_scores_00(self):
        self.assertEqual(calculate_trailhead_scores(load_input(filename='..\\inputs\\day10_short0.txt')), 2)
    
    def test_calculate_trailhead_scores_01(self):
        self.assertEqual(calculate_trailhead_scores(load_input(filename='..\\inputs\\day10_short1.txt')), 4)

    def test_calculate_trailhead_scores_02(self):
        self.assertEqual(calculate_trailhead_scores(load_input(filename='..\\inputs\\day10_short2.txt')), 3)

    def test_calculate_trailhead_scores_03(self):
        self.assertEqual(calculate_trailhead_scores(load_input(filename='..\\inputs\\day10_short3.txt')), 36)

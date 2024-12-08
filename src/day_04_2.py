#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '04 December 2024'
__version__ = '0.1.0'

import re
import unittest
import numpy as np


def load_input(filename: str) -> np.matrix:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split("\n")
    my_lines = np.matrix([[z for z in y] for y in my_lines])
    return my_lines


def find_directional_xmas(my_str: str) -> int:
    total = 0
    for index in range(len(my_str)):
        if my_str[index:index+4] == 'XMAS':
            total += 1
    return total


def find_xmas_in(my_str = str) -> int:
    return find_directional_xmas(my_str=my_str) + find_directional_xmas(my_str=my_str[::-1])


def count_by_rows(my_lines: np.matrix) -> int:
    sub_total = 0
    for row_index in range(my_lines.shape[0]):
        sub_total += find_xmas_in(''.join(my_lines[row_index,:].tolist()[0]))
    # print(f"Found {sub_total} XMASes by row")
    return sub_total


def count_by_columns(my_lines: np.matrix) -> int:
    sub_total = 0
    for col_index in range(my_lines.shape[1]):
        # print(f"Testing column {''.join(my_lines[:,col_index].flatten().tolist()[0])}")
        sub_total += find_xmas_in(''.join(my_lines[:,col_index].flatten().tolist()[0]))
    # print(f"Found {sub_total} XMASes by column")
    return sub_total


def count_by_diagonals(my_lines: np.matrix) -> int:
    sub_total = 0
    for col_index in range(my_lines.shape[1]):
        sub_total += find_xmas_in(''.join(my_lines.diagonal(offset=col_index).tolist()[0]))
    # print(f"Found {sub_total} XMASes by upper diagonals")
    for row_index in range(1, my_lines.shape[0]):
        sub_total += find_xmas_in(''.join(my_lines.diagonal(offset=-row_index).tolist()[0]))
    # print(f"Found {sub_total} XMASes by lower diagonals")
    return sub_total


def count_by_other_diagonals(my_lines: np.matrix) -> int:
    sub_total = 0
    for col_index in range(my_lines.shape[1]):
        sub_total += find_xmas_in(''.join(np.flipud(my_lines).diagonal(offset=col_index).tolist()[0]))
    # print(f"Found {sub_total} XMASes by upper diagonals")
    for row_index in range(1, my_lines.shape[0]):
        sub_total += find_xmas_in(''.join(np.flipud(my_lines).diagonal(offset=-row_index).tolist()[0]))
    # print(f"Found {sub_total} XMASes by lower diagonals")
    return sub_total


def count_xmas(my_lines: np.matrix) -> int:
    xmas_total = 0
    # check the horizontal lines first
    xmas_total += count_by_rows(my_lines=my_lines)
    # check the columns
    xmas_total += count_by_columns(my_lines=my_lines)
    # check the diagonals
    xmas_total += count_by_diagonals(my_lines=my_lines)
    xmas_total += count_by_other_diagonals(my_lines=my_lines)
    return xmas_total


def count_xmas_2(my_lines: np.matrix) -> int:
    xmas_total = 0
    for col_index in range(1, my_lines.shape[1]-1):
        for row_index in range(1, my_lines.shape[0]-1):
            if my_lines[row_index, col_index] == 'A':
                upper_left = my_lines[row_index-1, col_index-1]
                lower_right = my_lines[row_index+1, col_index+1]
                lower_left = my_lines[row_index-1, col_index+1]
                upper_right = my_lines[row_index+1, col_index-1]
                if (upper_left == 'M' and lower_right == 'S') or (upper_left == 'S' and lower_right == 'M'):
                    if (lower_left == 'M' and upper_right == 'S') or (lower_left == 'S' and upper_right == 'M'):
                        xmas_total += 1
    return xmas_total


def main():
    my_lines = load_input('..\\inputs\\day04.txt')
    result_0 = count_xmas(my_lines)
    print(f'XMAS appears {result_0} times.')
    result_1 = count_xmas_2(my_lines)
    print(f'XMAS appears {result_1} times.')


if __name__ == '__main__':
    main()


class TestDay04Methods(unittest.TestCase):

    def test_find_directional_xmas_01(self):
        self.assertEqual(find_directional_xmas('XMASAMX.MM'), 1)
    
    def test_find_directional_xmas_02(self):
        self.assertEqual(find_directional_xmas('XMASAMX.MM'[::-1]), 1)
    
    def test_find_xmas_in_01(self):
        self.assertEqual(find_xmas_in('XMASAMX.MM'), 2)

    def test_count_by_rows_01(self):
        self.assertEqual(count_by_rows(np.matrix([[x for x in 'XMASAMX.MM'], [x for x in 'XMASAMX.MM']])), 4)
    
    def test_count_by_columns_01(self):
        self.assertEqual(count_by_columns(np.matrix([
            [x for x in 'XMASXMASXMAS'],
            [x for x in 'MMASXMASXMAA'],
            [x for x in 'AMASXMASXMAM'],
            [x for x in 'SMASXMASXMAX']
        ])), 2)

    def test_count_by_diagonals_01(self):
        self.assertEqual(count_by_diagonals(np.matrix([
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
        ])), 1)
    
    def test_count_by_other_diagonals(self):
        self.assertEqual(count_by_other_diagonals(np.matrix([
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
            [x for x in 'XMAS'],
        ])), 1)
#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '01 December 2024'
__version__ = '0.1.0'

import re


def load_input(filename):
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split("\n")
    return my_lines


def find_difference_0(my_lines) -> int:
    total_difference = 0
    pairs = list()
    pairs.append(list())
    pairs.append(list())
    for each_line in my_lines:
        pairs[0].append(int(re.search('(\\d+)\\s+(\\d+)', each_line).group(1)))
        pairs[1].append(int(re.search('(\\d+)\\s+(\\d+)', each_line).group(2)))
    pairs[0].sort()
    pairs[1].sort()
    for index in range(len(my_lines)):
        total_difference += abs(pairs[0][index] - pairs[1][index])
    return total_difference


def sorted_fast_count(my_list: list, value: int) -> int:
    """
    Return the occurences of value in my_list, under the assumption that my_list is sorted in ascending order.
    """
    count = 0
    for each_value in my_list:
        if each_value == value:
            count += 1
        elif count > 0:
            break
    return count


def find_similarity_score(my_lines) -> int:
    total_similarity = 0
    pairs = list()
    pairs.append(list())
    pairs.append(list())
    for each_line in my_lines:
        pairs[0].append(int(re.search('(\\d+)\\s+(\\d+)', each_line).group(1)))
        pairs[1].append(int(re.search('(\\d+)\\s+(\\d+)', each_line).group(2)))
    pairs[0].sort()
    pairs[1].sort()
    for index in range(len(my_lines)):
        total_similarity += pairs[0][index] * sorted_fast_count(pairs[1], pairs[0][index])
    return total_similarity


def main():
    my_lines = load_input('..\\inputs\\day01.txt')
    result_0 = find_difference_0(my_lines)
    print(f"The total distance between the lists is {result_0}")
    result_1 = find_similarity_score(my_lines)
    print(f"The similarity score of the two lists is {result_1}")


if __name__ == '__main__':
    main()

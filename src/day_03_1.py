#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '03 December 2024'
__version__ = '0.1.0'

import re


def load_input(filename: str) -> str:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split("\n")
    my_lines = ''.join(my_lines)
    return my_lines


def execute_multiplications(my_lines: str) -> int:
    multiplication_sum = 0
    matches = re.finditer('mul\\((\\d{1,3}),(\\d{1,3})\\)', my_lines)
    for each_match in matches:
        multiplication_sum += int(each_match.group(1)) * int(each_match.group(2))
    return multiplication_sum


def main():
    my_lines = load_input('..\\inputs\\day03.txt')
    result_0 = execute_multiplications(my_lines)
    print(f"If you add up all of the results of the multiplications you get {result_0}")


if __name__ == '__main__':
    main()

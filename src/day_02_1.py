#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '02 December 2024'
__version__ = '0.1.0'

import re
import numpy as np
import pandas as pd


def load_input(filename):
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split("\n")
    return my_lines


def count_safe_reports(my_lines) -> int:
    safe_reports = 0
    for each_line in my_lines:
        report = np.array([0] + [int(x) for x in each_line.split(' ')])
        report = (report[1:] - report[:-1])[1:]
        if all([x < 0 for x in report]):
            report *= -1
        if any(x < 1 for x in report):
            continue
        if any(x > 3 for x in report):
            continue
        safe_reports += 1
    return safe_reports


def main():
    my_lines = load_input('..\\inputs\\day02.txt')
    result_0 = count_safe_reports(my_lines)
    print(f"The number of safe reports is {result_0}")


if __name__ == '__main__':
    main()

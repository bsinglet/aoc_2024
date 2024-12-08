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


def is_safe_report(report: np.array) -> bool:
    report = (report[1:] - report[:-1])[1:]
    if all([x < 0 for x in report]):
        report *= -1
    if any(x < 1 for x in report):
        return False
    if any(x > 3 for x in report):
        return False
    return True


def count_safe_reports_1(my_lines) -> int:
    safe_reports = 0
    for each_line in my_lines:
        report = [int(x) for x in each_line.split(' ')]
        for index in range(len(report)):
            temp_report = [0] + report[:index] + report[index+1:]
            temp_report = np.array(temp_report)
            if is_safe_report(temp_report):
                safe_reports += 1
                break        
    return safe_reports


def main():
    my_lines = load_input('..\\inputs\\day02.txt')
    result_0 = count_safe_reports(my_lines)
    print(f"The number of safe reports is {result_0}")
    result_1 = count_safe_reports_1(my_lines)
    print(f"The number of reports that are now safe is {result_1}")


if __name__ == '__main__':
    main()

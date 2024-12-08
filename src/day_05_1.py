#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2024'
__version__ = '0.1.0'

import re
import unittest
import numpy as np


def load_input(filename: str) -> tuple:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    ordering_rules, updates = my_lines.split("\n\n")
    ordering_rules = ordering_rules.split('\n')
    ordering_rules = [(int(x.split('|')[0]), int(x.split('|')[1])) for x in ordering_rules]
    updates = updates.split('\n')
    updates = [[int(y) for y in x.split(',')] for x in updates]
    return ordering_rules, updates


def find_correctly_ordered_updates(ordering_rules: list, updates: list) -> int:
    middle_page_sum = 0
    for each_update in updates:
        matched = True
        for each_rule in ordering_rules:
            if each_rule[0] in each_update and each_rule[1] in each_update:
                if each_update.index(each_rule[0]) > each_update.index(each_rule[1]):
                    # print(f"{each_update} fails because of {each_rule}: {each_update.index(each_rule[0])} > {each_update.index(each_rule[1])}")
                    matched = False
                    break
        if matched:
            middle_page_sum += each_update[int(len(each_update)/2)]
    return middle_page_sum


def main():
    ordering_rules, updates = load_input('..\\inputs\\day05.txt')
    result_0 = find_correctly_ordered_updates(ordering_rules=ordering_rules, updates=updates)
    print(f'The sum of the middle page numbers from the correctly-ordered updates is {result_0}.')


if __name__ == '__main__':
    main()

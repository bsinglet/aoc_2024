#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '05 December 2024'
__version__ = '0.1.0'

import re
import unittest
import functools
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


def find_correctly_ordered_updates_2(ordering_rules: list, updates: list) -> int:
    middle_page_sum = 0
    for each_update in updates:
        matched = True
        relevant_rules = get_relevant_rules(ordering_rules, each_update)
        for each_rule in relevant_rules:
            def rule_compare(element_0, element_1):
                less_rule = [x for x in relevant_rules if x[0] == element_0 and x[1] == element_1][0]
                greater_rule = [x for x in relevant_rules if x[0] == element_0 and x[1] == element_1][0]
                if less_rule is not None:
                    return 1
                elif greater_rule is not None:
                    return -1
                else:
                    return 0
            each_update = each_update.sort(key=functools.cmp_to_key())
            index_0 = each_update.index(each_rule[0])
            index_1 = each_update.index(each_rule[1])
                if index_0 > index_1:
                    # print(f"{each_update} fails because of {each_rule}: {each_update.index(each_rule[0])} > {each_update.index(each_rule[1])}")
                    # move the first term right before the first term
                    each_update = each_update[:index_1] + [each_rule[0]] + each_update[index_1:index_0] + each_update[index_0+1:]
                    matched = False
        if not matched:
            print(f"{each_update}")
            middle_page_sum += each_update[int(len(each_update)/2)]
    return middle_page_sum


def get_relevant_rules(ordering_rules: list, update: list) -> list:
    relevant = list()
    for each_rule in ordering_rules:
        if each_rule[0] in update and each_rule[1] in update:
            relevant.append(each_rule)
    return relevant


def construct_dependency_chain(ordering_rules: list, update: list) -> list:
    relevant_rules = get_relevant_rules(ordering_rules, update)
    sorted_list = list()


def main():
    ordering_rules, updates = load_input('..\\inputs\\day05.txt')
    result_0 = find_correctly_ordered_updates(ordering_rules=ordering_rules, updates=updates)
    print(f'The sum of the middle page numbers from the correctly-ordered updates is {result_0}.')
    result_1 = find_correctly_ordered_updates_2(ordering_rules=ordering_rules, updates=updates)
    print(f'The sum of the middle page numbers after correctly ordering the incorrectly-ordered updates is {result_1}.')


if __name__ == '__main__':
    main()

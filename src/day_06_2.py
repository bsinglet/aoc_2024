#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '06 December 2024'
__version__ = '0.1.0'

import re
import unittest
import numpy as np


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split('\n')
    my_lines = [[y for y in x] for x in my_lines]
    return my_lines


def find_distinct_positions(my_lines: list) -> int:
    # print(my_lines)
    distinct_positions = 0
    position = (-1, -1)
    momentum = (0, 0)
    # find the starting position
    for y in range(len(my_lines)):
        try:
            if my_lines[y].index('^'):
                position = (my_lines[y].index('^'), y)
                momentum = (0, -1)
        except:
            continue
    #print(f"Position: {position}, momentum: {momentum}")
    # simulate the guard's route until she leaves the mapped area
    #print(len(my_lines[0]))
    #print(len(my_lines))
    while position[0] >= 0 and position[0] < len(my_lines[0]) and position[1] >= 0 and position[1] < len(my_lines):
        """for each_row in my_lines:
            print(''.join(each_row))
        print()"""
        new_position = (position[0] + momentum[0], position[1] + momentum[1])
        if new_position[0] < 0 or new_position[0] >= len(my_lines[0]) or new_position[1] < 0 or new_position[1] >= len(my_lines):
            # leave the area
            my_lines[position[1]][position[0]] = 'X'
            break
        elif my_lines[new_position[1]][new_position[0]] != '#':
            # move forward
            my_lines[position[1]][position[0]] = 'X'
            position = new_position
        else:
            # turn 90 degrees
            if momentum == (0, -1):
                momentum = (1, 0)
            elif momentum == (1, 0):
                momentum = (0, 1)
            elif momentum == (0, 1):
                momentum = (-1, 0)
            elif momentum == (-1, 0):
                momentum = (0, -1)
            else:
                raise Exception('Unreachable reached')
    # count the Xs
    for each_row in my_lines:
        # print(''.join(each_row))
        distinct_positions += each_row.count('X')
    return distinct_positions


def update_cell(old: str, momentum: tuple) -> str:
    new_cell = ''
    if momentum == (0, -1):
        if old in ['-', '+']:
            new_cell = '+'
        else:
            new_cell = '|'
    elif momentum == (1, 0):
        if old in ['|', '+']:
            new_cell = '+'
        else:
            new_cell = '-'
    elif momentum == (0, 1):
        if old in ['-', '+']:
            new_cell = '+'
        else:
            new_cell = '|'
    elif momentum == (-1, 0):
        if old in ['|', '+']:
            new_cell = '+'
        else:
            new_cell = '-'
    else:
        raise Exception('Unreachable reached')
    return new_cell


def find_distinct_obstructions(my_lines: list) -> int:
    distinct_obstructions = 0
    position = (-1, -1)
    momentum = (0, 0)
    # find the starting position
    for y in range(len(my_lines)):
        try:
            if my_lines[y].index('^'):
                position = (my_lines[y].index('^'), y)
                momentum = (0, -1)
        except:
            continue
    print(position)
    print(momentum)
    my_lines[position[1]][position[0]] = '|'
    # map out the unobstructed path
    while position[0] >= 0 and position[0] < len(my_lines[0]) and position[1] >= 0 and position[1] < len(my_lines):
        """for each_row in my_lines:
            print(''.join(each_row))
        print()"""
        new_position = (position[0] + momentum[0], position[1] + momentum[1])
        if new_position[0] < 0 or new_position[0] >= len(my_lines[0]) or new_position[1] < 0 or new_position[1] >= len(my_lines):
            # leave the area
            my_lines[position[1]][position[0]] = update_cell(my_lines[position[1]][position[0]], momentum)
            break
        elif my_lines[new_position[1]][new_position[0]] != '#':
            # move forward
            my_lines[position[1]][position[0]] = update_cell(my_lines[position[1]][position[0]], momentum)
            position = new_position
        else:
            # turn 90 degrees
            if momentum == (0, -1):
                momentum = (1, 0)
                my_lines[position[1]][position[0]] = '+'
            elif momentum == (1, 0):
                momentum = (0, 1)
                my_lines[position[1]][position[0]] = '+'
            elif momentum == (0, 1):
                momentum = (-1, 0)
                my_lines[position[1]][position[0]] = '+'
            elif momentum == (-1, 0):
                momentum = (0, -1)
                my_lines[position[1]][position[0]] = '+'
            else:
                raise Exception('Unreachable reached')
    for each_row in my_lines:
        print(''.join(each_row))
    return distinct_obstructions


def main():
    my_lines = load_input('..\\inputs\\day06_short.txt')
    result_0 = find_distinct_positions(my_lines)
    print(f'The guard will visit {result_0} distinct positions before leaving the mapped area.')
    my_lines = load_input('..\\inputs\\day06_short.txt')
    result_1 = find_distinct_obstructions(my_lines)
    print(f'There are {result_1} different positions you could choose for this obstruction.')


if __name__ == '__main__':
    main()

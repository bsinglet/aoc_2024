#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '16 December 2024'
__version__ = '0.1.0'

import re
import unittest
import sympy as smp


def load_input(filename: str) -> list:
    my_lines = ''
    machines = list()
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split('\n\n')
    for each_machine in my_lines:
        each_machine = each_machine.split('\n')
        temp_machine = {'A_x': int(re.match('[^\\:]+:\\s+X\\+(\\d+),\\s+Y\\+(\\d+)', each_machine[0]).group(1)), 
                        'A_y': int(re.match('[^\\:]+:\\s+X\\+(\\d+),\\s+Y\\+(\\d+)', each_machine[0]).group(2))}
        temp_machine['B_x'] = int(re.match('[^\\:]+:\\s+X\\+(\\d+),\\s+Y\\+(\\d+)', each_machine[1]).group(1))
        temp_machine['B_y'] = int(re.match('[^\\:]+:\\s+X\\+(\\d+),\\s+Y\\+(\\d+)', each_machine[1]).group(2))
        temp_machine['P_x'] = int(re.match('[^\\:]+:\\s+X=(\\d+),\\s+Y=(\\d+)', each_machine[2]).group(1))
        temp_machine['P_y'] = int(re.match('[^\\:]+:\\s+X=(\\d+),\\s+Y=(\\d+)', each_machine[2]).group(2))
        machines.append(temp_machine)
    return machines


def minimum_for_machine(each_machine: dict) -> int:
    """
    Return the minimum number of tokens required to win the prize for this 
    machine, if possible. Return 0 if there is no prize.
    """
    minimum_tokens = 0
    a, b = smp.symbols('a b')
    solutions = smp.linsolve([each_machine['A_x'] * a + each_machine['B_x'] * b - each_machine['P_x'], each_machine['A_y'] * a + each_machine['B_y'] * b - each_machine['P_y']], (a, b))
    # print(f"{each_machine} solutions are {solutions}")
    if len(solutions) > 0:
        for each_solution in solutions:
            # make sure it's a whole integer solution
            if int(each_solution[0]) != each_solution[0] or int(each_solution[1]) != each_solution[1]:
                # print(f"{each_solution[0]}: {int(each_solution[0])}, {each_solution[1]}: {int(each_solution[1])}")
                continue
            cost = 3 * each_solution[0] + each_solution[1]
            if minimum_tokens == 0 or cost < minimum_tokens:
                minimum_tokens = cost
    return minimum_tokens


def find_minimum_tokens(machines: list) -> int:
    minimum_tokens = 0
    for each_machine in machines:
        minimum_tokens += minimum_for_machine(each_machine)
    return minimum_tokens


def main():
    filename = '..\\inputs\\day13.txt'
    machines = load_input(filename=filename)
    result_0 = find_minimum_tokens(machines)
    print(f'The fewest tokens you would have to spend to win all possible prizes is {result_0}.')


if __name__ == '__main__':
    main()


class TestDay12Methods(unittest.TestCase):
    def test_find_minimum_tokens_part_1_short(self):
        self.assertEqual(find_minimum_tokens(load_input(filename='..\\inputs\\day13_short.txt')), 480)
    
    def test_find_minimum_tokens_part_1_full(self):
        self.assertEqual(find_minimum_tokens(load_input(filename='..\\inputs\\day13.txt')), 26005)

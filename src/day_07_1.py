#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '08 December 2024'
__version__ = '0.1.0'


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = my_lines.split('\n')
    return my_lines


def evaluate(operands: list, operators: list) -> int:
    index = 0
    total = 0
    for each_operator in operators:
        if index == 0:
            if each_operator == '+':
                total = operands[index] + operands[index+1]
            elif each_operator == '*':
                total = operands[index] * operands[index+1]
            index = 2
        else:
            if each_operator == '+':
                total = total + operands[index]
            elif each_operator == '*':
                total = total * operands[index]
            index += 1
    return total


def find_valid_calibrations(my_lines: list) -> int:
    total_calibration_result = 0
    for each_line in my_lines:
        candidate_result = int(each_line.split(':')[0])
        operands = [int(x) for x in each_line.split(':')[1].strip().split(' ')]
        operators = ['*'] * (len(operands) - 1)
        while '*' in operators:
            # print(f"Testing {operands} {operators}")
            if evaluate(operands, operators) == candidate_result:
                # print(f"Winning line: {each_line}")
                total_calibration_result += candidate_result
                break
            # permutate the operators by converting to binary, subtracting 1, converting back to strings
            operators = ''.join(operators)
            # treat times as 1 and additions as 0
            operators = operators.replace('+', '0').replace('*', '1')
            # convert to binary and then subtract 1
            operators = bin(int(operators, base=2) - 1)[2:]
            # add back the leading 0s
            operators = ('0' * (len(operands) - 1 - len(operators))) + operators
            # convert back to operators
            operators = operators.replace('0', '+').replace('1', '*')
            # we need a list of operators, not a continuous string of them
            operators = [x for x in operators]
        else:
            # handle the case of addition only
            if evaluate(operands, operators) == candidate_result:
                # print(f"Winning line: {each_line}")
                total_calibration_result += candidate_result
            else:
                # print(f"Failed line: {each_line}")
                pass
    return total_calibration_result


def main():
    my_lines = load_input('..\\inputs\\day07.txt')
    result_0 = find_valid_calibrations(my_lines)
    print(f'The total calibration result is {result_0}.')
    # print(evaluate([11, 6, 16, 20], ['+', '*', '+']))


if __name__ == '__main__':
    main()

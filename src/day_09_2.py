#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '12 December 2024'
__version__ = '0.1.0'


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = [int(x) for x in my_lines]
    return my_lines


def process_disk_map(puzzle_input: list) -> list:
    """
    Turn the puzzle input into a list of file IDs and empty spaces.
    """
    disk_map = list()
    current_id = 0
    for each_index in range(0, len(puzzle_input), 2):
        disk_map = disk_map + [current_id] * puzzle_input[each_index]
        current_id += 1
        if each_index + 1 < len(puzzle_input):
            disk_map = disk_map + ['.'] * puzzle_input[each_index+1]
    # print(disk_map)
    return disk_map



def calculate_checksum(disk_map):
    checksum = 0
    for index in range(len(disk_map)):
        if disk_map[index] == '.':
            continue
        checksum += index * disk_map[index]
    return checksum


def calculate_final_checksum(puzzle_input: list) -> int:
    final_checksum = 0
    disk_map = process_disk_map(puzzle_input)
    right_index = len(disk_map)-1
    # move the right-most blocks to the first vacant free block 
    while right_index > disk_map.index('.'):
        if right_index != '.':
            disk_map[disk_map.index('.')] = disk_map[right_index]
            disk_map[right_index] = '.'
        right_index -= 1
    # now calculate the checksum of the resulting disk
    final_checksum = calculate_checksum(disk_map)
    return final_checksum


def calculate_final_checksum_2(puzzle_input: list) -> int:
    final_checksum = 0
    file_id = 0
    location = 0
    file_locations = dict()
    free_space = list()
    for index in range(len(puzzle_input)):
        file_locations[file_id] = {'size': puzzle_input[index], 'position': location}
        location += puzzle_input[index]
        file_id += 1
        if index + 1 <= len(puzzle_input):
            free_space.append({'size': puzzle_input[index], 'position': location})
            location += puzzle_input[index]
    # move the right-most blocks to the first vacant free block 
    while file_id > 0:
        free_block = None
        for each_block in free_space:
            if each_block['size'] >= file_locations[file_id]['size']:
                file_locations[file_id]['position'] = each_block['positon']
                if each_block['size'] >=
        if free_block and free_block < file_locations[file_id]['position']:
            file_locations[file_id]['position'] = index
    # now calculate the checksum of the resulting disk
    final_checksum = calculate_checksum(disk_map)
    return final_checksum


def main():
    filename = '..\\inputs\\day09_short.txt'
    disk_map = load_input(filename=filename)
    result_0 = calculate_final_checksum(disk_map)
    print(f'The resulting checksum is {result_0}.')
    disk_map = load_input(filename=filename)
    result_1 = calculate_final_checksum_2(disk_map)
    print(f'The resulting checksum is {result_1}.')


if __name__ == '__main__':
    main()

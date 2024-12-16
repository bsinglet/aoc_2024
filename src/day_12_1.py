#!/usr/bin/python
__author__ = 'Benjamin M. Singleton'
__date__ = '15 December 2024'
__version__ = '0.1.0'

import unittest
from tqdm import tqdm


def load_input(filename: str) -> list:
    my_lines = ''
    with open(filename, 'r') as my_file:
        my_lines = my_file.read()
    my_lines = my_lines.strip()
    my_lines = [[y for y in x] for x in my_lines.split('\n')]
    return my_lines


def get_regions(my_lines: list) -> list:
    """
    Given the map of the garden, return a list of lists, where each sublist 
    contains all the coordinate pairs for a contiguous region of plants.
    """
    map_x = len(my_lines[0])
    map_y = len(my_lines)
    regions = list()
    visited = list()
    pending_locations = list()
    pending_regions = list()
    current_location = (0, 0)
    current_region = list()
    while len(set(visited)) < len(my_lines) * len(my_lines[0]):
        if current_location in visited:
            if len(pending_locations) > 0:
                # we still have more locations to visit in this region.
                current_location = pending_locations.pop()
            elif len(pending_regions) > 0:
                # we've visited every location in this region, but there are unvisited neighbors outside this region
                if len(current_region) > 0:
                    regions.append(current_region)
                current_location = pending_regions.pop()
                current_region = list()
            else:
                break
        current_region.append(current_location)
        visited.append(current_location)
        neighbors = [(current_location[0]-1, current_location[1]),
                     (current_location[0]+1, current_location[1]),
                     (current_location[0], current_location[1]-1),
                     (current_location[0], current_location[1]+1)]
        # check each neighbor to make sure it's in-map, not visited or queued up
        # already, and then file it away as in the same region or a separate one
        for each_neighbor in neighbors:
            if each_neighbor not in visited and each_neighbor not in pending_locations \
                and each_neighbor[0] >= 0 and each_neighbor[0] < map_x:
                if each_neighbor[1] >= 0 and each_neighbor[1] < map_y:
                    if my_lines[current_location[1]][current_location[0]] == my_lines[each_neighbor[1]][each_neighbor[0]]:
                        pending_locations.append(each_neighbor)
                    else:
                        pending_regions.append(each_neighbor)
        if len(pending_locations) > 0:
            # we still have more locations to visit in this region.
            current_location = pending_locations.pop()
        elif len(pending_regions) > 0:
            # we've visited every location in this region, but there are unvisited neighbors outside this region
            if len(current_region) > 0:
                regions.append(current_region)
            current_location = pending_regions.pop()
            current_region = list()
        else:
            print("Uhh")
    print(f"Visited {len(visited)} spaces, but only {len(set(visited))} were unique")
    total_spaces = 0
    for index, each_region in enumerate(regions):
        # print(f"Region {index}: {len(each_region)} spaces")
        total_spaces += len(each_region)
    print(f"Accounted for {total_spaces} spaces out of {len(my_lines) * len(my_lines[0])}")
    return regions


def total_fencing_price(my_lines: list) -> int:
    """
    Given the map of the garden, calculate the total fencing price one region
    at a time. In each region, the price is equal to the area * perimeter 
    (including any internal fences.)
    """
    fencing_price = 0
    all_regions = get_regions(my_lines)
    for each_region in all_regions:
        perimeter = 0
        # each square in a region contributes 4-n to the perimeter, where n is
        # the number of neighbors it has in the same region. For example, a 
        # square surrounded by the same plants has no fencing on it. If it has
        # three like neighbors, it needs a fence on 1 side, etc.
        for each_location in each_region:
            num_neighbors = 0
            neighbors = [(each_location[0]-1, each_location[1]),
                         (each_location[0]+1, each_location[1]),
                         (each_location[0], each_location[1]-1),
                         (each_location[0], each_location[1]+1)]
            for each_neighbor in neighbors:
                if each_neighbor in each_region:
                    num_neighbors += 1
            perimeter += 4 - num_neighbors
        fencing_price += perimeter * len(each_region)
    return fencing_price


def main():
    filename = '..\\inputs\\day12.txt'
    my_lines = load_input(filename=filename)
    result_0 = total_fencing_price(my_lines)
    print(f'The total price of fencing all regions on my map is {result_0}.')


if __name__ == '__main__':
    main()


class TestDay12Methods(unittest.TestCase):
    def test_total_fencing_price_00(self):
        self.assertEqual(total_fencing_price(load_input(filename='..\\inputs\\day12_short0.txt')), 140)
    
    def test_total_fencing_price_01(self):
        self.assertEqual(total_fencing_price(load_input(filename='..\\inputs\\day12_short1.txt')), 772)
    
    def test_total_fencing_price_02(self):
        self.assertEqual(total_fencing_price(load_input(filename='..\\inputs\\day12_short2.txt')), 1930)
"""
@Author: Jonathan Thomas
@Version: 3/20/17
@Description: islands.py contains a method, process,
               which returns the minimum number of islands on a far-away planet.
               L represents land, so if L's are connected and C's are
               connected to the L's, they make up one island.
"""
from collections import deque


def make_2d_array(my_list):
    return list(map(list, my_list))


def check_l_or_c(my_list, row, column):
    if my_list[row][column] == 'L' or my_list[row][column] == 'C':
        # return true if letter we're testing is a cloud or land
        return True
    return False  # not land or cloud. Return false


def test_neighbors(my_list, row, column):
    visited_queue = deque()
    visited_queue.append((row, column))

    while visited_queue:
        row_num, column_num = visited_queue.pop()

        # mark the location as visited
        my_list[row_num][column_num] = 'V'

        if row_num - 1 >= 0:  # check above
            if check_l_or_c(my_list, row_num - 1, column_num):
                visited_queue.append((row_num - 1, column_num))

        if column_num - 1 >= 0:  # check left
            if check_l_or_c(my_list, row_num, column_num - 1):
                visited_queue.append((row_num, column_num - 1))

        if row_num + 1 < len(my_list):  # check below
            if check_l_or_c(my_list, row_num + 1, column_num):
                visited_queue.append((row_num + 1, column_num))

        if column_num + 1 < len(my_list[row_num]):  # check right
            if check_l_or_c(my_list, row_num, column_num + 1):
                visited_queue.append((row_num, column_num + 1))


def process(my_list):
    # none case
    if my_list is None:
        return -1
    elif not my_list:
        return 0
    else:
        island_count = 0

        # make list into 2D character array. Easier to manipulate
        two_d_list = make_2d_array(my_list)

        for i in range(0, len(two_d_list)):
            for j in range(0, len(two_d_list[i])):
                letter = two_d_list[i][j]
                # first, find the first instance of land
                if letter == 'L':
                    island_count += 1
                    # find either land or clouds connected to the land
                    test_neighbors(two_d_list, i, j)
        return island_count

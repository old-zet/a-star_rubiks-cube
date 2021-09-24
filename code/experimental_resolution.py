#!/usr/bin/env python
# coding: utf-8

"""Various functions feeding A*.
"""

from classical_resolution import *
from relevant_operators import *
from rubiks_a_star import *


# Limit the number of turns to optimize get_mult_path().
TURN_LIMIT = 15
# Depth limit for the hybrid method (Python's max is 989).
LIM = 45
# Number of allowed paths.
NB_PATH = 50


def select_square(cube, y, x):
    """Find the possible advantageous squares for every wrong square.
    """
    sol = []
    coord = side_coordinates_by_value(FINAL_STATE, cube[y][x])
    for i in range(coord[0], coord[0] + 3):
        for j in range(coord[1], coord[1] + 3):
            if cube[i][j]!=cube[y][x]:
                pos = [i, j]
                sol.append(pos)
    return sol


def compare_found_path(a, path):
    """Compares two paths.
    """
    res = 0
    for b in path:
        if len(a)==len(b):
            size = 0
            while size<len(b):
                if a[size][0]!=b[size][0]:
                    res += 1.
                    break
                size += 1
        else:
            res += 1
    return res


def get_square(cube):
    """Find the first wrong square's position.
    """
    for i in range(0, len(cube)):
        for j in range(0, len(cube[i])):
            if i<=2 and cube[i][j]!="W":
                pos = [i, j]
                return pos
            elif i>=6 and cube[i][j]!="Y":
                pos = [i, j]
                return pos
            elif i>=3 and i<6:
                if j in range(0, 3) and cube[i][j]!="G":
                    pos = [i, j]
                    return pos
                elif j in range(3, 6) and cube[i][j]!="R":
                    pos = [i, j]
                    return pos
                elif j in range(6, 9) and cube[i][j]!="B":
                    pos = [i, j]
                    return pos
                elif j in range(9, 12) and cube[i][j]!="O":
                    pos = [i, j]
                    return pos
    return None


def get_path(cube, lim, path, pos, dest_pos):
    """Get a list of possible paths 
    between wrong and advantageous squares.
    """
    if pos==dest_pos:
        return []
    elif lim==0:
        return []
    operations = find_available_operators(pos)
    applicables = applicable_operators(operations, cube, pos)
    for ope in applicables:
        l_ope = apply_operator(ope, cube)
        new_pos = ope[1](cube, pos[0], pos[1])
        path = get_path(l_ope, lim - 1, path, new_pos, dest_pos)
        if path is not None and lim==LIM:
            path.append(ope)
            if path:  # Secondary path search.
                a = compare_found_path(path, path)  # Compare two paths.
                if a==len(path):
                    return path
                else:
                    continue
            else:
                return path
        elif path is not None:
            return [ope]+path
    return None


def get_mult_path(cube, lim, pos, destination):
    """Get a list of 4/5 possible paths between 
    the wrong and advantageous squares,
    such squares must differ by color.
    """
    path = []
    turn_limit = 0
    while len(path)<NB_PATH and turn_limit<TURN_LIMIT:
        turn_limit += 1
        action_list = []
        action_list = get_path(cube, lim, path, pos, destination)
        if action_list:  # Store found paths.
            path.append(action_list)
    i = 1
    for a in path:
        i += 1
        for b in a:
            continue
    return path


def hybrid(cube, limit, final_path):
    """Recursive hybrid A*-DFS method to optimize the search.
    """
    if is_final(cube) or limit==0:
        return cube
    false_square_position = get_square(cube)
    positions_cases_destination = select_square(
        cube, 
        false_square_position[0], 
        false_square_position[1]
    )
    copy = copy_cube(cube)
    possible_paths = get_mult_path(
        copy, 
        limit, 
        false_square_position, 
        positions_cases_destination[0]
        )
    while len(possible_paths):  # Test each path.
        kept_path = a_star(cube, possible_paths)  # Apply A*.
        if len(kept_path)==0:
            positions_cases_destination.pop(0)
            possible_paths = get_mult_path(
                copy, 
                available_operators, 
                limit, 
                false_square_position, 
                positions_cases_destination[0]
            )
        else:
            possible_paths = []
    copy = copy_cube(cube)
    cube = apply_path(cube, kept_path)
    print('Progression:', log_solution_progression(cube))
    final_path.append(kept_path)
    limit = limit-1  # Decrement on depth.
    cube = hybrid(cube, limit, final_path)

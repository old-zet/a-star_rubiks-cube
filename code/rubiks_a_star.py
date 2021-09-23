#!/usr/bin/env python
# coding: utf-8

"""Define a valid A* function to tackle 
the 3x3 Rubik's cube solution.
"""

from classical_resolution import *
from experimental_resolution import *


def a_star(cube, open_paths):
    """A* algorithm where f(n) = g(n) + h(n).
    """
    print('Initiating A*')
    print("Number of open paths: ", len(open_paths))
    if open_paths is None or len(open_paths)==0:
        return None
    kept_path = open_paths[0]
    copy = apply_path(copy_cube(cube), kept_path)
    left_kept_progression = left_progression(copy)
    for i in range(len(open_paths)):
        copy = apply_path(copy_cube(cube), open_paths[i])
        left_current_progression = left_progression(copy)
        if left_current_progression==0:
            return open_paths[i]
        if (
            find_best_path(open_paths[i], left_current_progression) < 
            find_best_path(kept_path, left_kept_progression)
        ):
            kept_path = open_paths[i]
            left_kept_progression = left_current_progression
    return kept_path


def left_progression(cube):
    """Number of remaining squares to be analyzed, which is
    equivalent to the h parameter in the A* theory.
    """
    return 54-log_solution_progression(cube)


def find_best_path(path, left_progression):
    """Compute the performance score, the lower 
    this score, the more efficient A* is and the 
    lower the number of squares to be analyzed.
    """
    return len(path)+left_progression


def apply_path(cube, path):
    """Loop over apply_operator().
    """
    for ope in path:
        cube = apply_operator(ope, cube)
    return cube

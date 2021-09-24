#!/usr/bin/env python
# coding: utf-8

"""Solve Rubik's cube from a given initial state.
"""

import time

from experimental_resolution import *
from operators import *
from operator_preconditions import *
from classical_resolution import *


# 3 moves to mix it well enough. More moves means higher difficulty.
initial_state = copy_cube(FINAL_STATE)
initial_state = vrotate2(initial_state)
initial_state = vrotate2(initial_state)
initial_state = rotate_face_side_inv(initial_state)
# Initial logging.
print("Initial state:")
state_to_text(initial_state)
# A switch for hybrid method testing.
star_test = False
# For time measures.
start = time.time()
if star_test:  # Hybrid method.
    final_path = []
    # Test 1.
    res = hybrid(initial_state, LIM, final_path)
    print_solution(initial_state, res, state_to_text)
else:
    # Test 2.
    # res = depth_limited_search(initial_state, is_final, available_operators, 5)
    # Test 3.
    # res = depth_first_memory_search(initial_state, is_final, available_operators, state_to_text, {})
    # Test 4.
    # res = breadth_first_search(initial_state, is_final, available_operators)
    # Test 5.
    # res = depth_first_search(initial_state, is_final, available_operators)
    # Test 6.
    res = depth_first_iterative_search(initial_state, is_final, available_operators)
    # Test 7.
    # res = depth_first_random_search(initial_state, is_final, available_operators)
    print_solution(initial_state, res, state_to_text)
end = time.time()
print(f'Time elapsed: {end-start}')

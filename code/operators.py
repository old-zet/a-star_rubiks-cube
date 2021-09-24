#!/usr/bin/env python
# coding: utf-8

"""All the Rubik's cube's possible operators.
"""

import random

from classical_resolution import new_operator


# Modified values to track rotations visually.
DEBUG_STATE = [
    ['0a', '1a', '2a'],
    ['3a', '4a', '5a'],
    ['6a', '7a', '8a'],
    ['0b', '1b', '2b', '0d', '1d', '2d', '0e', '1e', '2e', '0f', '1f', '2f'],
    ['3b', '4b', '5b', '3d', '4d', '5d', '3e', '4e', '5e', '3f', '4f', '5f'],
    ['6b', '7b', '8b', '6d', '7d', '8d', '6e', '7e', '8e', '6f', '7f', '8f'],
    ['0c', '1c', '2c'],
    ['3c', '4c', '5c'],
    ['6c', '7c', '8c']
]
# Initial state is given in main.
FINAL_STATE = [
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['G', 'G', 'G', 'R', 'R', 'R', 'B', 'B', 'B', 'O', 'O', 'O'],
    ['G', 'G', 'G', 'R', 'R', 'R', 'B', 'B', 'B', 'O', 'O', 'O'],
    ['G', 'G', 'G', 'R', 'R', 'R', 'B', 'B', 'B', 'O', 'O', 'O'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y'],
    ['Y', 'Y', 'Y']
]


def copy_cube(cube):
    """Copy Rubik's cube at any given state.
    """
    copy = []
    for i in range(0, len(cube)):
        tmp_copy = []  # Temporary list.
        for j in range(0, len(cube[i])):
            tmp_copy.append(cube[i][j])
        copy.append(tmp_copy)
    return copy


def print_cube(cube):
    """Print the cube, mainly for tests.
    """
    for i in range(0, len(cube)):
        print(cube[i])
    return


def is_final(s):
    """Check if a given state is the final one.
    """
    return (s==FINAL_STATE)


def precond_always_true(s):
    """Set the precondition to use a 
    given operator as true at any state.
    """
    return True
    

def vrotate(state, n, dif):
    """Rotate Rubik's vertical lines given
    the indices of the affected squares and 
    the differences between two sides.
    """
    copy_state = copy_cube(state)
    for i in range(3, len(state)):
        copy_state[i][n] = state[i-3][n]
    copy_state[i-3][n + dif] = state[i-2][n]
    copy_state[i-4][n + dif] = state[i-1][n]
    copy_state[i-5][n + dif] = state[i][n]
    copy_state[i-6][n] = state[i-5][n+dif]
    copy_state[i-7][n] = state[i-4][n+dif]
    copy_state[i-8][n] = state[i-3][n+dif]
    return copy_state


def vrotate1(state):
    """First possible vertical rotation.
    """
    return vrotate(state, 0, 8)


def vrotate2(state):
    """Second possible vertical rotation.
    """
    return vrotate(state, 1, 6)


def vrotate3(state):
    """Third possible vertical rotation.
    """
    return vrotate(state, 2, 4)


def vrotate_inv(state, n, dif):
    """Rotate Rubik's vertical lines in reverse.
    """
    for _ in range(3):
        state = vrotate(state, n, dif)
    return state


def vrotate_inv1(state):
    """Forth possible vertical rotation.
    """
    return vrotate_inv(state, 0, 8)


def vrotate_inv2(state):
    """Fifth possible vertical rotation.
    """
    return vrotate_inv(state, 1, 6)


def vrotate_inv3(state):
    """Sixth possible vertical rotation.
    """
    return vrotate_inv(state, 2, 4)


def hrotate(state):
    """Rotate Rubik's horizontal lines.
    """
    copy_state = copy_cube(state)
    for i in range(3, len(state)):
        copy_state[i] = state[i-3]
    for j in range(9, len(state)):
        copy_state[j-9] = state[j]
    return copy_state


def hrotate1(state):
    """First possible horizontal rotation.
    """
    state[3] = hrotate(state[3])
    return state


def hrotate2(state):
    """Second possible horizontal rotation.
    """
    state[4] = hrotate(state[4])
    return state


def hrotate3(state):
    """Third possible horizontal rotation.
    """
    state[5] = hrotate(state[5])
    return state


def hrotate_inv(state):
    """Rotate Rubik's horizontal lines in reverse.
    """
    for _ in range(3):
        state = hrotate(state)
    return state


def hrotate_inv1(state):
    """Forth possible horizontal rotation.
    """
    state[3] = hrotate_inv(state[3])
    return state


def hrotate_inv2(state):
    """Fifth possible horizontal rotation.
    """
    state[4] = hrotate_inv(state[4])
    return state


def hrotate_inv3(state):
    """Sixth possible horizontal rotation.
    """
    state[5] = hrotate_inv(state[5])
    return state


def rotate_down_side_base(state, l=0):  # l is 0 for more optimized permutations.
    """Rotate Rubik's top/down sides.
    """
    copy_state = copy_cube(state)
    copy_state[l+2][0] = state[l][0]
    copy_state[l+2][1] = state[l+1][0]
    copy_state[l+2][2] = state[l+2][0]
    copy_state[l+1][2] = state[l+2][1]
    copy_state[l][2] = state[l+2][2]
    copy_state[l][1] = state[l+1][2]
    copy_state[l][0] = state[l][2]
    copy_state[l+1][0] = state[l][1]
    return copy_state


def rotate_right_side_base(state, l=3, n=3):  # l and n are 3 for more optimized permutations as well.
    """Rotate Rubik's left/right sides.
    """
    copy_state = copy_cube(state)
    copy_state[l][n] = state[l+2][n]
    copy_state[l][n+1] = state[l+1][n]
    copy_state[l][n+2] = state[l][n]
    copy_state[l+1][n+2] = state[l][n+1]
    copy_state[l+2][n+1] = state[l+1][n+2]
    copy_state[l+2][n] = state[l+2][n+2]
    copy_state[l+1][n] = state[l+2][n+1]
    copy_state[l+2][n+2] = state[l][n+2]
    return copy_state


def rotate_down_side(state):
    """First possible down side rotation.
    """
    return rotate_right_side_base(hrotate3(state), 6, 0)


def rotate_down_side_inv(state):
    """Second possible down side rotation.
    """
    copy_state = hrotate_inv3(state)
    for _ in range(3):
        copy_state = rotate_right_side_base(copy_state, 6, 0)
    return copy_state


def rotate_top_side(state):
    """First possible top side rotation.
    """
    return rotate_right_side_base(hrotate_inv1(state), 0, 0)


def rotate_top_side_inv(state):
    """Second possible top side rotation.
    """
    copy_state = hrotate1(state)
    for _ in range(3):
        copy_state = rotate_right_side_base(copy_state, 0, 0)
    return copy_state


def rotate_right_side(state):
    """First possible right side rotation.
    """
    return rotate_right_side_base(vrotate_inv3(state))


def rotate_right_side_inv(state):
    """Second possible right side rotation.
    """
    copy_state = vrotate3(state)
    for _ in range(3):
        copy_state = rotate_right_side_base(copy_state)
    return copy_state


def rotate_left_side(state):
    """First possible left side rotation.
    """
    return rotate_right_side_base(vrotate1(state), 3, 9)


def rotate_left_side_inv(state):
    """Second possible left side rotation.
    """
    copy_state = vrotate_inv1(state)
    for _ in range(3):
        copy_state = rotate_right_side_base(copy_state, 3, 9)
    return copy_state


def vrotate_arriere(state):
    """Rotate Rubik's back side.
    """
    copy_state = copy_cube(state)
    copy_state[5][9] = state[0][0]
    copy_state[5][5] = state[8][0]
    copy_state[4][9] = state[0][1]
    copy_state[4][5] = state[8][1]
    copy_state[3][9] = state[0][2]
    copy_state[3][5] = state[8][2]
    copy_state[0][0] = state[3][5]
    copy_state[0][1] = state[4][5]
    copy_state[0][2] = state[5][5]
    copy_state[8][0] = state[3][9]
    copy_state[8][1] = state[4][9]
    copy_state[8][2] = state[5][9]
    return copy_state


def rotate_back_side(state):
    """First possible back side rotation.
    """
    return rotate_right_side_base(vrotate_arriere(state), 3, 6)


def rotate_back_side_inv(state):
    """Second possible back side rotation.
    """
    for _ in range(3):
        state = rotate_back_side(state)
    return state


def vrotate_face(state):
    """Rotate Rubik's front side.
    """
    copy_state = copy_cube(state)
    copy_state[3][3] = state[2][0]
    copy_state[4][3] = state[2][1]
    copy_state[5][3] = state[2][2]
    copy_state[6][2] = state[3][3]
    copy_state[2][2] = state[3][11]
    copy_state[6][1] = state[4][3]
    copy_state[2][1] = state[4][11]
    copy_state[6][0] = state[5][3]
    copy_state[2][0] = state[5][11]
    copy_state[3][11] = state[6][0]
    copy_state[4][11] = state[6][1]
    copy_state[5][11] = state[6][2]
    return copy_state


def rotate_face_side(state):
    """First possible front side rotation.
    """
    return rotate_right_side_base(vrotate_face(state), 3, 0)


def rotate_face_side_inv(state):
    """Second possible front side rotation.
    """
    for _ in range(3):
        state = rotate_face_side(state)
    return state


def vrotate_midline(state):
    """First possible horizontal midline rotation.
    """
    copy_state = copy_cube(state)
    copy_state[3][4] = state[1][0]
    copy_state[4][4] = state[1][1]
    copy_state[5][4] = state[1][2]
    copy_state[7][2] = state[3][4]
    copy_state[7][1] = state[4][4]
    copy_state[7][0] = state[5][4]
    copy_state[5][10] = state[7][2]
    copy_state[4][10] = state[7][1]
    copy_state[3][10] = state[7][0]
    copy_state[1][0] = state[5][10]
    copy_state[1][1] = state[4][10]
    copy_state[1][2] = state[3][10]
    return copy_state


def vrotate_midline_inv(state):
    """Second possible horizontal midline rotation.
    """
    for _ in range(3):
        state = vrotate_midline(state)
    return state


def random_apply():
    """Apply rotation operators randomly.
    """
    functions = [
        rotate_top_side,
        rotate_top_side_inv,
        rotate_down_side,
        rotate_down_side_inv,
        rotate_right_side,
        rotate_right_side_inv,
        rotate_left_side,
        rotate_left_side_inv,
        rotate_back_side,
        rotate_back_side_inv,
        rotate_face_side,
        rotate_face_side_inv,
        vrotate2,
        vrotate_inv2,
        vrotate_midline,
        vrotate_midline_inv,
        hrotate2,
        hrotate_inv2
    ]
    for _ in range(5):  # Change for more randomness.
        random.choice(functions)(FINAL_STATE)
    return FINAL_STATE


# Available operators to feed the search algorithms (precondition always true).
# For a version with variable preconditions, cf. operator_preconditions.
available_operators = [
    new_operator(
        "Vertical midline", 
        precond_always_true, 
        vrotate2
    ),
    new_operator(
        "Reverse vertical midline", 
        precond_always_true, 
        vrotate_inv2
    ),
    new_operator(
        "Perpendicular vertical midline", 
        precond_always_true, 
        vrotate_midline
    ),
    new_operator(
        "Reverse perpendicular vertical midline", 
        precond_always_true, 
        vrotate_midline_inv
    ),
    new_operator(
        "Horizontal midline", 
        precond_always_true, 
        hrotate2
    ),
    new_operator(
        "Reverse horizontal midline", 
        precond_always_true, 
        hrotate_inv2
    ),
    new_operator(
        "Top side", 
        precond_always_true, 
        rotate_top_side
    ),
    new_operator(
        "Reverse top side", 
        precond_always_true, 
        rotate_top_side_inv
    ),
    new_operator(
        "Down side", 
        precond_always_true, 
        rotate_down_side
    ),
    new_operator(
        "Reverse down side", 
        precond_always_true, 
        rotate_down_side_inv
    ),
    new_operator(
        "Right side", 
        precond_always_true, 
        rotate_right_side
    ),
    new_operator(
        "Reverse right side", 
        precond_always_true, 
        rotate_right_side_inv
    ),
    new_operator(
        "Left side", 
        precond_always_true, 
        rotate_left_side
    ),
    new_operator(
        "Reverse left side", 
        precond_always_true, 
        rotate_left_side_inv
    ),
    new_operator(
        "Back side", 
        precond_always_true, 
        rotate_back_side
    ),
    new_operator(
        "Reverse back side", 
        precond_always_true, 
        rotate_back_side_inv
    ),
    new_operator(
        "Front side", 
        precond_always_true, 
        rotate_face_side
    ),
    new_operator(
        "Reverse front side", 
        precond_always_true, 
        rotate_face_side_inv
    )
]

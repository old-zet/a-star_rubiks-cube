#!/usr/bin/env python
# coding: utf-8

"""Evaluate each available and applicable 
operator to find the best and most relevant 
to apply at a given Rubik's state.
"""

from operator_preconditions import *


# Coordinates of the first square for each side. 
TOP = [0,0]
DOWN = [6,0]
FRONT = [3,0]
RIGHT= [3,3]
BACK = [3,6]
LEFT = [3,9]


def side_coordinates_by_value(cube, square):
    """Modify Rubik's coordinates by a given value.
    """
    for i in range(0, len(cube)):
        for j in range(0, len(cube[i])):
            if cube[i][j]==square:
                return [i, j]
    return []


def side_coordinates_by_position(pos):
    """Evaluate Rubik's coordinates by a given value.
    """
    i = pos[0]-pos[0]%3
    j = pos[1]-pos[1]%3
    return [i, j]


def find_front(side_coordinates, available_operators):
    """Evaluate every available operator 
    as applicable or not on the front side.
    """
    if side_coordinates==TOP:
        available_operators.append(new_operator(
            "Top side", 
            test_rotate_top_side, 
            rotate_top_side)
        )
        available_operators.append(new_operator(
            "Reverse top side", 
            test_rotate_top_side_inv, 
            rotate_top_side_inv))
    elif side_coordinates==DOWN:
        available_operators.append(new_operator(
            "Down side", 
            test_rotate_down_side, 
            rotate_down_side)
        )
        available_operators.append(new_operator(
            "Reverse down side", 
            test_rotate_down_side_inv, 
            rotate_down_side_inv)
        )
    elif side_coordinates==FRONT:
        available_operators.append(new_operator(
            "Front side", 
            test_rotate_face_side, 
            rotate_face_side))
        available_operators.append(new_operator(
            "Reverse front side", 
            test_rotate_face_side_inv, 
            rotate_face_side_inv)
        )
    elif side_coordinates==RIGHT:
        available_operators.append(new_operator(
            "Right side", 
            test_rotate_right_side, 
            rotate_right_side)
        )
        available_operators.append(new_operator(
            "Reverse right side", 
            test_rotate_right_side_inv, 
            rotate_right_side_inv)
        )
    elif side_coordinates==BACK:
        available_operators.append(new_operator(
            "Back side", 
            test_rotate_back_side, 
            rotate_back_side)
        )
        available_operators.append(new_operator(
            "Reverse back side", 
            test_rotate_back_side_inv, 
            rotate_back_side_inv)
        )
    elif side_coordinates==LEFT:
        available_operators.append(new_operator(
            "Left side", 
            test_rotate_left_side, 
            rotate_left_side)
        )
        available_operators.append(new_operator(
            "Reverse left side", 
            test_rotate_left_side_inv, 
            rotate_left_side_inv)
        )
    return available_operators


def find_top(side_coordinates, available_operators):
    """Evaluate every available operator 
    as applicable or not on the top side.
    """
    if side_coordinates==TOP:
        available_operators.append(new_operator(
            "Back side", 
            test_rotate_back_side, 
            rotate_back_side)
        )
        available_operators.append(new_operator(
            "Reverse back side", 
            test_rotate_back_side_inv, 
            rotate_back_side_inv)
        )
    elif side_coordinates==DOWN:
        available_operators.append(new_operator(
            "Down side", 
            test_rotate_down_side, 
            rotate_down_side)
        )
        available_operators.append(new_operator(
            "Reverse down side", 
            test_rotate_down_side_inv, 
            rotate_down_side_inv)
        )
    elif (
        side_coordinates==FRONT or 
        side_coordinates==RIGHT or 
        side_coordinates==BACK or 
        side_coordinates==LEFT
    ):
        available_operators.append(new_operator(
            "Top side", 
            test_rotate_top_side, 
            rotate_top_side)
        )
        available_operators.append(new_operator(
            "Reverse top side", 
            test_rotate_top_side_inv, 
            rotate_top_side_inv)
        )
    return available_operators


def find_down(side_coordinates, available_operators):
    """Evaluate every available operator 
    as applicable or not on the down side.
    """
    if side_coordinates==TOP:
        available_operators.append(new_operator(
            "Front side", 
            test_rotate_face_side, 
            rotate_face_side)
        )
        available_operators.append(new_operator(
            "Reverse front side", 
            test_rotate_face_side_inv, 
            rotate_face_side_inv)
        )
    elif side_coordinates==DOWN:
        available_operators.append(new_operator(
            "Back side", 
            test_rotate_back_side, 
            rotate_back_side)
        )
        available_operators.append(new_operator(
            "Reverse back side", 
            test_rotate_back_side_inv, 
            rotate_back_side_inv))
    elif (
        side_coordinates==FRONT or 
        side_coordinates==RIGHT or 
        side_coordinates==BACK or 
        side_coordinates==LEFT):
        available_operators.append(new_operator(
            "Down side", 
            test_rotate_down_side, 
            rotate_down_side))
        available_operators.append(new_operator(
            "Reverse down side", 
            test_rotate_down_side_inv, 
            rotate_down_side_inv)
        )
    return available_operators


def find_right(side_coordinates, available_operators):
    """Evaluate every available operator 
    as applicable or not on the right side.
    """
    if (
        side_coordinates==TOP or 
        side_coordinates==DOWN or 
        side_coordinates==FRONT
    ):
        available_operators.append(new_operator(
            "Right side", 
            test_rotate_right_side, 
            rotate_right_side)
        )
        available_operators.append(new_operator(
            "Reverse right side", 
            test_rotate_right_side_inv, 
            rotate_right_side_inv)
        )
    elif side_coordinates==BACK:
        available_operators.append(new_operator(
            "Left side", test_rotate_left_side, 
            rotate_left_side)
        )
        available_operators.append(new_operator(
            "Reverse left side", 
            test_rotate_left_side_inv, 
            rotate_left_side_inv))
    elif side_coordinates==RIGHT:
        available_operators.append(new_operator(
            "Back side", 
            test_rotate_back_side, 
            rotate_back_side)
        )
        available_operators.append(new_operator(
            "Reverse back side", 
            test_rotate_back_side_inv, 
            rotate_back_side_inv)
        )
    elif side_coordinates==LEFT:
        available_operators.append(new_operator(
            "Front side", 
            test_rotate_face_side, 
            rotate_face_side)
        )
        available_operators.append(new_operator(
            "Reverse front side", 
            test_rotate_face_side_inv, 
            rotate_face_side_inv)
        )
    return available_operators


def find_left(side_coordinates, available_operators):
    """Evaluate every available operator 
    as applicable or not on the left side.
    """
    if (
        side_coordinates==TOP or 
        side_coordinates==DOWN or 
        side_coordinates==FRONT
    ):
        available_operators.append(new_operator(
            "Left side", 
            test_rotate_left_side, 
            rotate_left_side)
        )
        available_operators.append(new_operator(
            "Left side Reverse", 
            test_rotate_left_side_inv, 
            rotate_left_side_inv)
        )
    elif side_coordinates==BACK:
        available_operators.append(new_operator(
            "Right side", 
            test_rotate_right_side, 
            rotate_right_side)
        )
        available_operators.append(new_operator(
            "Reverse right side", 
            test_rotate_right_side_inv, 
            rotate_right_side_inv)
        )
    elif side_coordinates==RIGHT:
        available_operators.append(new_operator(
            "Front side", 
            test_rotate_face_side, 
            rotate_face_side)
        )
        available_operators.append(new_operator(
            "Reverse front side", 
            test_rotate_face_side_inv, 
            rotate_face_side_inv)
        )
    elif side_coordinates==LEFT:
        available_operators.append(new_operator(
            "Back side", 
            test_rotate_back_side, 
            rotate_back_side)
        )
        available_operators.append(new_operator(
            "Reverse back side", 
            test_rotate_back_side_inv, 
            rotate_back_side_inv)
        )
    return available_operators


def find_vrotate(side_coordinates, available_operators):
    """Evaluate every available operator as 
    applicable or not on the vertical slices.
    """
    if (
        side_coordinates==TOP or 
        side_coordinates==DOWN or 
        side_coordinates==FRONT or 
        side_coordinates==BACK
    ):
        available_operators.append(new_operator(
            "Vertical midline", 
            test_vrotate2, 
            vrotate2)
        )
        available_operators.append(new_operator(
            "Reverse vertical midline", test_vrotate_inv2, vrotate2))
    elif (side_coordinates == RIGHT or side_coordinates == LEFT):
        available_operators.append(new_operator(
            "Perpendicular vertical midline", 
            test_vrotate_midline, 
            vrotate_midline)
        )
        available_operators.append(new_operator(
            "Reverse perpendicular vertical midline", 
            test_vrotate_midline_inv, 
            vrotate_midline_inv)
        )

    return available_operators


def find_hrotate(side_coordinates, available_operators):
    """Evaluate every available operator as 
    applicable or not on the horizontal slices.
    """
    if side_coordinates==TOP or side_coordinates==DOWN:
        available_operators.append(new_operator(
            "Perpendicular vertical midline", 
            test_vrotate_midline, 
            vrotate_midline)
        )
        available_operators.append(new_operator(
            "Reverse perpendicular vertical midline", 
            test_vrotate_midline_inv, 
            vrotate_midline_inv)
        )
        available_operators.append(new_operator(
            "Vertical midline", 
            test_vrotate2, 
            vrotate2))
        available_operators.append(new_operator(
            "Reverse vertical midline", 
            test_vrotate_inv2, 
            vrotate2)
        )
    elif (
        side_coordinates==FRONT or 
        side_coordinates==BACK or 
        side_coordinates==RIGHT or 
        side_coordinates==LEFT
    ):
        available_operators.append(new_operator(
            "Horizontal midline", 
            test_hrotate2, 
            hrotate2)
        )
        available_operators.append(new_operator(
            "Reverse horizontal midline", 
            test_hrotate_inv2, 
            hrotate_inv2)
        )
    return available_operators


def find_available_operators(square_coordinates):
    """Find the best operators to 
    apply in a given Rubik's state.
    """
    side_coordinates_square = side_coordinates_by_position(
        square_coordinates
    )
    available_operators = []
    available_operators = find_front(
        side_coordinates_square, 
        available_operators
    )
    if square_coordinates[0]%3==0:
        available_operators = find_top(
            side_coordinates_square, 
            available_operators
        )
    elif square_coordinates[0]%3==1:
        available_operators = find_hrotate(
            side_coordinates_square, 
            available_operators
        )
    elif square_coordinates[0]%3==2:
        available_operators = find_down(
            side_coordinates_square, 
            available_operators
        )
    if square_coordinates[1]%3==0:
        available_operators = find_left(
            side_coordinates_square, 
            available_operators
        )
    elif square_coordinates[1]%3==1:
        available_operators = find_vrotate(
            side_coordinates_square, 
            available_operators
        )
    elif square_coordinates[1]%3==2:
        available_operators = find_right(
            side_coordinates_square, 
            available_operators
        )
    return available_operators

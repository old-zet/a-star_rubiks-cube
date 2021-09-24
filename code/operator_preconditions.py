#!/usr/bin/env python
# coding: utf-8

"""Preconditions to attempt to tackle the complexity issues
which appear when mixing the Rubik's cube into a hard-to-solve 
state, i.e. when the tree-depth becomes exponential.
"""

from operators import *


def test_vrotate(state, y, x, n, dif):
    """Test the vertical rotation operators given
    the indices of the affected squares and 
    the differences between two sides.
    """
    for i in range(3, len(state)):
        if (i-3)==y and n==x:
            return [i, n]
    i = len(state)-1
    if x==n:
        if y==(i-2):
            return [(i-3), (n+dif)]
        elif y==(i-1):
            return [(i-4), (n+dif)]
        elif y==i:
            return [(i-5), (n+dif)]
    elif x==(n+dif):
        if y==(i-5):
            return [(i-6), n]
        elif y==(i-4):
            return [(i-7), n]
        elif y==(i-3):
            return [(i-8), n]
    return [y, x]


def test_vrotate1(state, y, x):
    """Test the first possible vertical rotation.
    """
    if x!=0 and x!=8:
        return [y, x]
    pos = test_vrotate(state, y, x, 0, 8)
    if state[pos[0]][pos[1]]!=state[y][x]:
        return pos
    return [y, x]


def test_vrotate2(state, y, x):
    """Test the second possible vertical rotation.
    """
    if x!=1 and x!=7:
        return [y, x]
    pos = test_vrotate(state, y, x, 1,6)
    if state[pos[0]][pos[1]]!=state[y][x]:
        return pos
    return [y, x]


def test_vrotate3(state, y, x):
    """Test the third possible vertical rotation.
    """
    if x!=2 and x!=6:
        return [y, x]
    pos = test_vrotate(state, y, x, 2, 4)
    if state[pos[0]][pos[1]]!=state[y][x]:
        return pos
    return [y, x]


def test_vrotate_inv(state, y, x, n, dif):
    """Test the reverse vertical rotation operators 
    given the indices of the affected squares and 
    the differences between two sides.
    """
    pos = [y, x]
    for _ in range(3):
        pos = test_vrotate(state, pos[0], pos[1], n, dif)
    return pos


def test_vrotate_inv1(state, y, x):
    """Test the forth possible vertical rotation.
    """
    if x!=0 and x!=8:
        return [y, x]
    return test_vrotate_inv(state, y, x, 0, 8)


def test_vrotate_inv2(state, y, x):
    """Test the fifth possible vertical rotation.
    """
    if x!=1 and x!=7:
        return [y, x]
    pos = test_vrotate_inv(state, y, x, 1, 6)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_vrotate_inv3(state, y, x):
    """Test the sixth possible vertical rotation.
    """
    if x!=2 and x!=6:
        return [y, x]
    return test_vrotate_inv(state, y, x, 2, 4)


def test_hrotate(state, x):
    """Test the horizontal rotation operators given
    the indices of the affected squares and 
    the differences between two sides.
    """
    for i in range(3, len(state)):
        if i-3==x:
            return i
    for j in range(9, len(state)):
        if j==x:
            return j-9
    return x


def test_hrotate1(state, y, x):
    """Test the first possible horizontal rotation.
    """
    if y!=3:
        return [y, x]
    z = test_hrotate(state[3], x)
    if state[3][z]!=state[y][x]:
        return [3, z]
    return [y, x]


def test_hrotate2(state, y, x):
    """Test the second possible horizontal rotation.
    """
    if y!=4:
        return [y, x]
    z = test_hrotate(state[4], x)
    if state[4][z]!=state[y][x]:
        return [4, z]
    return [y, x]


def test_hrotate3(state, y, x):
    """Test the third possible horizontal rotation.
    """
    if y!=5:
        return [y, x]
    z = test_hrotate(state[5], x)
    if state[5][z]!=state[y][x]:
        return [5, z]
    return [y, x]


def test_hrotate_inv(state, x):
    """Test the reverse horizontal rotation operators.
    """
    nouv_state = copy_cube(state)
    pos = x
    for _ in range(3):
        nouv_state = hrotate(nouv_state)
        pos = test_hrotate(nouv_state, pos)
    return pos


def test_hrotate_inv1(state, y, x):
    """Test the forth possible horizontal rotation.
    """
    if y!=3:
        return [y, x]
    z = test_hrotate_inv(state[3], x)
    if state[3][z]!=state[y][x]:
        return [3, z]
    return [y, x]


def test_hrotate_inv2(state, y, x):
    """Test the fifth possible horizontal rotation.
    """
    if y!=4:
        return [y, x]
    z = test_hrotate_inv(state[4], x)
    if state[4][z]!=state[y][x]:
        return [4, z]
    return [y, x]


def test_hrotate_inv3(state, y, x):
    """Test the sixth possible horizontal rotation.
    """
    if y!=5:
        return [y, x]
    z = test_hrotate_inv(state[5], x)
    if state[5][z]!=state[y][x]:
        return [5, z]
    return [y, x]


def test_rotate_down_side(y, x, l=0):
    """Test the Rubik's top/down sides rotations.
    """
    if x==0:
        if y==l:
            return [(l+2), 0]
        elif y==(l+1):
            return [(l+2), 1]
        elif y==(l+2):
            return [(l+2), 2]
    elif x==1:
        if y==l:
            return [(l+1), 0]
        elif y==(l+2):
            return [(l+1), 2]
    elif x==2:
        if y==l:
            return [l, 0]
        elif y==(l+2):
            return [l, 2]
        elif y==(l+1):
            return [l, 1]
    return [y, x]


def test_rotate_right_side_base(y, x, l=3, n=3):
    """Test the Rubik's left/right sides rotations.
    """
    if y==l:
        if x==n:
            return [l, n+2]
        elif x==(n+1):
            return [l+1, n+2]
        elif x==(n+2):
            return [l+2, n+2]
    elif y==(l+1):
        if x==n:
            return [l, n+1]
        elif x==(n+2):
            return [l+2, n+1]
    elif y==(l+2):
        if x==n:
            return [l, n]
        elif x==(n+1):
            return [l+1, n]
        elif x==(n+2):
            return [l+2, n]
    return [y, x]


def test_rotate_down_side(state, y, x):
    """Test the first possible down side rotation.
    """
    pos = test_hrotate3(state, y, x)
    pos = test_rotate_right_side_base(pos[0], pos[1], 6, 0)
    if state[pos[0]][pos[1]]!=state[y][x]:
        return pos
    return [y, x]


def test_rotate_top_side_inv(state, y, x):
    """Test the second possible top side rotation.
    """
    pos = [y, x]
    pos = test_hrotate1(state, pos[0], pos[1])
    for _ in range(3):
        pos = test_rotate_right_side_base(pos[0], pos[1], 0, 0)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_down_side_inv(state, y, x):
    """Test the first possible down side rotation.
    """
    pos = [y, x]
    pos = test_hrotate_inv3(state, pos[0], pos[1])
    for _ in range(3):
        pos = test_rotate_right_side_base(pos[0], pos[1], 6, 0)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_top_side(state, y, x):
    """Test the second possible top side rotation.
    """
    pos = test_hrotate_inv1(state, y, x)
    pos = test_rotate_right_side_base(pos[0], pos[1], 0, 0)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_right_side(state, y, x):
    """Test the first possible right side rotation.
    """
    pos = test_vrotate_inv3(state, y, x)
    pos = test_rotate_right_side_base(pos[0], pos[1])
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_right_side_inv(state, y, x):
    """Test the second possible right side rotation.
    """
    pos = [y, x]
    pos = test_vrotate3(state, pos[0], pos[1])
    for _ in range(3):
        pos = test_rotate_right_side_base(pos[0], pos[1])
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_left_side(state, y, x):
    """Test the first possible left side rotation.
    """
    pos = [y, x]
    pos = test_vrotate1(state, pos[0], pos[1])
    pos = test_rotate_right_side_base(pos[0], pos[1], 3, 9)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_left_side_inv(state, y, x):
    """Test the second possible left side rotation.
    """
    pos = [y, x]
    pos = test_vrotate_inv1(state, pos[0], pos[1])
    for _ in range(3):
        pos = test_rotate_right_side_base(pos[0], pos[1], 3, 9)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_vrotate_arriere(y, x):
    """Test the back side vertical rotations.
    """
    i = y
    j = x
    if y==0:
        j = 9
    elif y==8:
        j = 5
    elif y==3:
        j = 0
    elif y==4:
        j = 1
    elif y==5:
        j = 2
    else:
        j = x
    if x==0:
        i = 5
    elif x==1:
        i = 4
    elif x==2:
        i = 3
    elif x==5:
        i = 0
    elif x==9:
        i = 8
    else:
        i = y
    return [i, j]


def test_rotate_back_side(state, y, x):
    """Test the first possible back side rotation.
    """
    pos = test_vrotate_arriere(y, x)
    pos = test_rotate_right_side_base(pos[0], pos[1], 3, 6)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_back_side_inv(state, y, x):
    """Test the second possible back side rotation.
    """
    for _ in range(3):
        pos = test_rotate_back_side(state, y, x)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_vrotate_face(state, y, x):
    """Test the front side vertical rotations.
    """
    i = y
    j = x
    if y==2 and x in (0, 1, 2):
        return [x+3, 3]
    if y==6 and x in (0, 1, 2):
        return [x+3, 11]
    if x==3 and y in (3, 4, 5):
        i = 6
    elif x==11 and y in (3, 4, 5):
        i = 2
    if y==3 and x in (3, 11):
        j = 2
    elif y==4 and x in (3, 11):
        j = 1
    elif y==5 and x in (3, 11):
        j = 0
    return [i, j]


def test_rotate_face_side(state, y, x):
    """Test the first possible front side rotation.
    """
    pos = test_vrotate_face(state, y, x)
    pos = test_rotate_right_side_base(pos[0], pos[1], 3, 0)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_rotate_face_side_inv(state, y, x):
    """Test the second possible front side rotation.
    """
    pos = [y, x]
    for _ in range(3):
        pos = test_vrotate_face(state, pos[0], pos[1])
        pos = test_rotate_right_side_base(pos[0], pos[1], 3, 0)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_vrotate_midline_base(y, x):
    """Test the midline vertical rotations.
    """
    old_x = x
    old_y = y
    if old_x>=0 and old_x<=2:
        x = old_y+3
        y = old_x+3
        return [y, x]
    if old_x==4:
        y = 7
    elif old_x==10:
        y = 1
    if old_y==3:
        x = 2
    elif old_y==4:
        x = 1
    elif old_y==5:
        x = 0
    return [y, x]


def test_vrotate_midline(state, y, x):
    """Test the first possible midline vertical rotation.
    """
    pos = test_vrotate_midline_base(y, x)
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]


def test_vrotate_midline_inv(state, y, x):
    """Test the second possible midline vertical rotation.
    """
    pos = [y, x]
    for _ in range(3):
        pos = test_vrotate_midline_base(pos[0], pos[1])
    if state[y][x]!=state[pos[0]][pos[1]]:
        return pos
    return [y, x]

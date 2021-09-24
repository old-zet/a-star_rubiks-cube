#!/usr/bin/env python
# coding: utf-8

"""Various DFS and BFS functions, as well as 
logging solutions (no external libraries used).
"""

import random


def new_operator(n, p, a):
    """Construct a new operator.
    """
    return (n, p, a)


def operator_name(o):
    """Access operator's name.
    """
    return o[0]


def operator_precondition(o):
    """Access operator's precondition.
    """
    return o[1]


def operator_action(o):
    """Access operator's action.
    """
    return o[2]


def is_applicable(o, s, pos):
    """Test if a given operator is applicable at a given Rubik's state.
    """
    precond = operator_precondition(o)
    if pos!=[]:  # Positional calculation to adapt to a given state.
        return precond(s, pos[0], pos[1])!=pos
    return precond(s)


def applicable_operators(os, s, pos = []):
    """Get a list of (advantageous) operators 
    applicable at a given Rubik's state.
    """
    res = []
    for o in os:
        if is_applicable(o, s, pos):
            res.append(o)
    return res


def apply_operator(o, s):
    """Apply a given operator to a given Rubik's state.
    """
    action = operator_action(o)
    cube = action(s)
    return cube


def state_to_text(s):
    """Print the cube at a given state in a non-list format.
    """
    for i in s:
        print(*i)
    print('\n')
    return


def print_solution(s, os, txtstate):
    """Print the found solution.
    """
    if os==None:
        print("No solution")
    else:
        for o in os:
            print("\n")
            print(operator_name(o))  # Operator's name.
            s = apply_operator(o, s)
            print(txtstate(s))  # New state.


def depth_first_search(s, is_final, os):
    """Recursive DFS from a given state 
    with a list of available operators.
    """
    if is_final(s):
        return []
    else:
        applicables = applicable_operators(os, s)  # Search applicable operators.
        for o in applicables:
            succ = apply_operator(o, s)
            path = depth_first_search(succ, is_final, os)
            if path is not None:
                return [o]+path
        return None


def depth_limited_search(s, is_final, os, lim):
    """Recursive DFS from a given state, 
    with a list of available operators 
    and maximum depth limit to avoid loops.  
    """
    if is_final(s):
        return []
    elif lim == 0:
        return None
    else:
        applicables = applicable_operators(os, s)
        for o in applicables:
            succ = apply_operator(o, s)
            path = depth_limited_search(succ, is_final, os, lim-1)
            if path is not None:
                return [o]+path
        return None


def depth_first_iterative_search(s, is_final, os):
    """Recursive DFS from a given state, with a list of 
    available operators and a manually adjustable 
    maximum depth limit to optimize the search.  
    """
    limit = 0  # Initial limit.
    result = None
    while result==None:
        result = depth_limited_search(s, is_final, os, limit)
        limit = limit+1  # Increment at every loop.
    return result


def depth_first_random_search(s, is_final, os):
    """Recursive DFS from a given state, with 
    a list of available operators and a randomly 
    shuffled applicable operators.  
    """
    if is_final(s):
        return []
    else:
        applicables = applicable_operators(os, s)
        random.shuffle(applicables)  # Mix applicable operators.
        for o in applicables:
            succ = apply_operator(o, s)
            path = depth_first_random_search(succ, is_final, os)
            if path is not None:
                    return [o]+path
        return None


def depth_first_memory_search(s, is_final, os, txtstate, already_seen):
    """Recursive DFS from a given state, with 
    a list of available operators and a memorization 
    process for the paths already traveled through.
    """
    if is_final(s):
        return []
    else:
        statetxt = txtstate(s)
        if statetxt in already_seen:
            return None
        else:
            already_seen[statetxt] = 1
            applicables = applicable_operators(os, s)
            for o in applicables:
                succ = apply_operator(o, s)
                path = depth_first_memory_search(
                    succ, 
                    is_final, 
                    os, 
                    txtstate, 
                    already_seen
                )
                if path is not None:
                    return [o]+path
            return None


def breadth_first_search(s, is_final, os):
    """BFS taking into account open and 
    closed Rubik's states, as well as 
    applicable operators at any given moment.
    """
    opened = [s]
    closed = []
    success = False
    while opened and not success:
        n = opened.pop(0)
        if is_final(n):
            success = True
        else:
            closed.append(n)
            applicables = applicable_operators(os, s)
            for o in applicables:
                succ = apply_operator(o, n)
                if succ not in closed:
                    opened.append(succ)
                if is_final(succ):
                    return [o] 
            return None


def log_solution_progression(cube):
    """A* logging solution which evaluates algorithm's 
    success rate by 54 (N of Rubik's squares).
    """
    progression = 0
    for i in range(0, len(cube)):
        for j in range(0, len(cube[i])):
            if i <= 2 and cube[i][j] == "W":  # Test each color starting with white.
                progression += 1
            elif i >= 6 and cube[i][j] == "Y":
                progression += 1
            else:
                if j in range(0, 3) and cube[i][j] == "G":
                    progression += 1
                elif j in range(3, 6) and cube[i][j] == "R":
                    progression += 1
                elif j in range(6, 9) and cube[i][j] == "B":
                    progression += 1
                elif j in range(9, 12) and cube[i][j] == "O":
                    progression += 1
    return progression

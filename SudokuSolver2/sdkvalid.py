""" Sdkvalid contains a set of functions to validate rows and generate missing numbers"""

import numpy as np

solved_sudoku = [
            [7,8,4,  1,5,9,  3,2,6],
            [5,3,9,  6,7,2,  8,4,1],
            [6,1,2,  4,3,8,  7,5,9],

            [9,2,8,  7,1,5,  4,6,3],
            [3,5,7,  8,4,6,  1,9,2],
            [4,6,1,  9,2,3,  5,8,7],

            [8,7,6,  3,9,4,  2,1,5],
            [2,4,3,  5,6,1,  9,7,8],
            [1,9,5,  2,8,7,  6,3,4]
        ]

not_solved_sudoku = [
    [7,0,0,  0,0,0,  0,0,6],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,8,  0,0,0],

    [0,0,8,  0,0,0,  0,0,0],
    [0,5,0,  8,0,6,  0,0,0],
    [0,0,0,  0,2,0,  0,0,0],

    [0,0,0,  0,0,0,  0,1,0],
    [0,4,0,  5,0,0,  0,0,0],
    [0,0,5,  0,0,7,  0,0,4]
]

solved_sdk = np.array(solved_sudoku)
not_solved_sdk = np.array(not_solved_sudoku)

def missing_values(row: list) -> list:
    """ Takes a list and returns a list of missing values.
    If there are no missing values, it returns []
    In that case, the row is correct """
    test_list = [1,2,3,4,5,6,7,8,9]
    return [number for number in test_list if number not in row]

def get_qdr(cell, sdk):
    """
    Gets the cell coordinate and returns a list of all the numbers
    in that quadrant
    TODO: re-format function to numpy native version
    """
    quadrant_list = []
    qdr = [int(cell[0]/3), int(cell[1]/3)]

    for x in range(qdr[0]*3,qdr[0]*3+3):
        for y in range(qdr[1]*3,qdr[1]*3+3):
            quadrant_list.append(sdk[x, y])
    return quadrant_list

def mv_cell(cell ,sdk):
    missing_row = set (missing_values( sdk[cell[0],:] ) )
    missing_column = set (missing_values( sdk[:, cell[1] ] ))
    missing_qdr = set (missing_values (get_qdr(cell, sdk)))
    all_missing_values = missing_row.intersection(missing_column, missing_qdr)
    return sorted(list(all_missing_values))

def mv_matrix(sdk):
    """ Returns a numpy object array with potential values for all EMPTY cells"""
    """ For cells with a value, it returns that value"""
    """ EXAMPLE IMPLEMENTATION
    m = missing_values_matrix(not_solved_sdk) -> returns matrix with all values
    q = get_qdr((0,0), m) -> returns a list with all missing values for each cell for a quadrant
    m[0, :] -> returns all missing values in a row.
    """
    empty = np.empty((9,9),dtype=object)
    for x in range(0,9):
        for y in range (0,9):
            if sdk[x,y]:
                empty[x,y] = [ sdk[x,y] ]
            else:
                empty[x,y] = mv_cell((x,y),sdk)
    return empty

def mv_solution_space_size(values_sdk):
    """
    Input: matrix with potential values for each cell.
    Returns a numpy object array with number of potential values for all EMPTY cells
    For cells with only one possible value, it returns a 1.
    Potential uses:
    np.sum (mv_solution_space_size(values_sdk)) == 81 -> this is a valid Sudoku solution.
    np.sum (mv_solution_space_size(values_sdk1)) <  np.sum (mv_solution_space_size(values_sdk2))
    -> sdk1 represents a smaller solution space than sdk2
    """
    f = lambda x: len(x)
    vf = np.vectorize(f)
    return vf(values_sdk)

m = mv_matrix(solved_sdk)
print(mv_solution_space_size(m))
print(np.sum(mv_solution_space_size(m)))

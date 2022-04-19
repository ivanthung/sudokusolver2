import sdkloader
import numpy as np
import sdkstrat

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

def main():
    sdk_database = sdkloader.load_sdk(5, 'hard')
    a = sdkstrat.simple_recursion(not_solved_sdk)
    print(a)

if __name__ == '__main__':
    main()

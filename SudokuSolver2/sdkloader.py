"""
Request an x amount of Sudoku's by difficulty rating.
Returns a list of np arrays with the requested amount of Sudoku's
"""
import numpy as np

hard_txt = '../data/sudoku-exchange-puzzle-bank/hard.txt'
medium_txt = '../data/sudoku-exchange-puzzle-bank/medium.txt'
easy_txt = '../data/sudoku-exchange-puzzle-bank/easy.txt'

def get_one(
    sdk_obj: str ) -> np.array:

    sdk_obj = sdk_obj.split()
    sdk_pzl = np.array( [n for n in sdk_obj[1]]
                       ).reshape(9,9)

    # sdk_id = sdk_obj[0]
    # sdk_difficulty = sdk_obj[2] -- atm  no use for this rating and id might be useful later,
    return sdk_pzl

def load_sdk(amount=1, difficulty = 'easy') -> list:
    file = eval(difficulty + '_txt')
    with open(file) as myfile:
        sdk_list = [next(myfile) for x in range(0, amount)]
    return [get_one(sdk) for sdk in sdk_list]

print(load_sdk(10, 'hard'))

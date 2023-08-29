"""
This module contains the tictactoeLineCombo class which is a class that represents the
winning line combination of a tictactoe game.
"""

class tictactoeLineCombo:
    def __init__(self):
        pass

    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  # horiz.
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  # vertical
        [1, 5, 9],
        [3, 5, 7],  # diagonal
    ]



    @staticmethod
    def itemInIterables(item, sequences):
        """Function that returns a tuple of indexes for which item is in iterable
        
           Parameters
           ==========
           item is the item to search for in a sequence. Even though function was
           designed for int sequences it is mentioned in the Python documentation
           that your functions should be flexible in design and I like to stick
           to good practices and design patterns. This means function does work
           with sequences of strings or other data types.
           
           sequences contain multiple sequences ie multiple lists or tuples
           
           Returns
           =======
           A sequence of indexes in int format in which item is found within sequences.
           
           for example take if the move is 1 then it is possible to win by three possible
           lines which are 
           
    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  # horiz.
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  # vertical
        [1, 5, 9],
        [3, 5, 7],  # diagonal
    ]

        If item is 1 then function will return all sequences that contain 1 which is [1,2,3], [1,4,7] and [1,5,9]
        """
        result = []
        i = 0
        for seq in sequences:
            if item in seq:
                result.append(i)
            i += 1

        return result

    @staticmethod
    def moveAffectedLines():
        """Function returns a dictionary of all affected lines by grid number. The key will be 
           grid number or move and the value are array indexes of the affected sequence as a list.
           
           For example grid 1 should be {1,[0,3,6]} because 1 is contained in the first sequence which
           starts at 0, fourth sequence so index is 3, and 7th sequence so index is 6. For grid 1
           it is possible to win by 3 possible lines. 
           
           Parameters
           ==========
           None
           
           Returns
           =======
           This function returns all affected lines for grid numbers 1 - 9 using dictionary comprehension."""

        return {i:tictactoeLineCombo.itemInIterables(i, tictactoeLineCombo.WIN_LINES) for i in range(1, 10)}


affectedLinesByGrid = tictactoeLineCombo.moveAffectedLines()






import unittest


test_1 = [[1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 2]]

test_2 = [[0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 0, 2],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0]]

test_3 = [[0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 1, 1, 1, 2],
          [0, 0, 0, 0, 1, 1, 1, 1]]

test_4 = [[0, 0, 2, 2, 2, 2, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 1, 1, 1, 2],
          [0, 0, 0, 0, 1, 2, 1, 1]]

test_5 = [[1, 0, 0, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 0, 0, 0, 2],
          [0, 0, 1, 0, 0, 0, 0, 1],
          [0, 0, 0, 1, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 2],
          [0, 0, 0, 0, 2, 1, 1, 1]]

test_6 = [[0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 2],
          [0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 2, 1, 1, 1, 2],
          [0, 0, 0, 0, 0, 1, 1, 1]]

test_7 = [[0, 0, 0, 0, 2, 0, 0, 1],
          [0, 0, 0, 0, 0, 2, 0, 2],
          [0, 0, 0, 0, 0, 0, 2, 1],
          [0, 0, 0, 0, 1, 0, 0, 2],
          [0, 0, 0, 0, 0, 2, 0, 0],
          [0, 0, 0, 2, 1, 1, 1, 2],
          [0, 0, 0, 0, 1, 2, 1, 1]]
          
test_8 = [[0, 0, 0, 1, 2, 0, 0, 1],
          [0, 0, 1, 0, 0, 1, 0, 2],
          [0, 1, 0, 0, 0, 0, 2, 1],
          [1, 0, 0, 0, 1, 0, 0, 2],
          [0, 0, 0, 0, 0, 2, 0, 0],
          [0, 0, 0, 2, 1, 1, 1, 2],
          [0, 0, 0, 0, 1, 2, 1, 1]]

test_9 = [[0, 0, 0, 1, 2, 0, 0, 1],
          [0, 0, 2, 0, 0, 1, 0, 2],
          [0, 1, 0, 0, 0, 0, 2, 1],
          [1, 0, 0, 2, 1, 0, 0, 2],
          [0, 0, 2, 0, 0, 2, 0, 0],
          [0, 2, 0, 2, 1, 1, 1, 2],
          [2, 0, 0, 0, 1, 2, 1, 1]]

def check_win(board):
        """check if there is four pieces in a row, column or diagonal. If there is, return the player number, else return 0"""
        # check rows
        for row in board:
            for i in range(5):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != 0:
                    return row[i]
        
        # check columns
        for column in range(8):
            for row in range(4):
                if board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column] != 0:
                    return board[row][column]
        
        # check diagonals
        for row in range(4):
            for column in range(5):
                if board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3] != 0:
                    return board[row][column]
        
        # diagonal from right to left
        for row in range(4):
            for column in range(7, 2, -1):  # to check from right to left
                if board[row][column] == board[row+1][column-1] == board[row+2][column-2] == board[row+3][column-3] != 0:
                    return board[row][column]

        return 0    # return 0 if there is no winner

class GameWinTest(unittest.TestCase):

    def test_vertical(self):
        self.assertEqual(check_win(test_1), 2)
        self.assertEqual(check_win(test_2), 1)

    def test_horizontal(self):
        self.assertEqual(check_win(test_3), 1)
        self.assertEqual(check_win(test_4), 2)
    
    def test_diagonal(self):
        self.assertEqual(check_win(test_5), 1)
        self.assertEqual(check_win(test_6), 1)
        self.assertEqual(check_win(test_7), 2)
        self.assertEqual(check_win(test_8), 1)
        self.assertEqual(check_win(test_9), 2)

        
if __name__ == '__main__':
    unittest.main()
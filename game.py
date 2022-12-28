# develeop the game and its functions here + 
# 2d array which has 7 rows and 8 columns + 
# 0 means empty, 1 means player 1, 2 means player 2 + 

# player will select a column to drop the piece, the piece will drop to the lowest empty row + 
# play will win if there are 4 pieces in a row, column or diagonal + 

# get possible moves function will return a list of possible moves, which are the columns that are not full + 
class Game:
    """All functions related with the game will be defined here,
        including the board, the moves, the win conditions, etc.
        """
        
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(7)]
    
    def make_move(self, player, column):
        for i in range(6, -1, -1):  # start checking from the bottom, if the column is not full, drop the piece there
            if self.board[i][column] == 0:
                self.board[i][column] = player
                return True     # return True if the move is successful
        return False        # return False if the move is not successful, which means the column is full
    
    def get_possible_moves(self):
        possible_moves = [idx  for idx, val in enumerate(self.board[0]) if val == 0]
        return possible_moves       # return a list which contains the indices of the columns that are not full
        
    def check_win(self):
        """check if there is four pieces in a row, column or diagonal. If there is, return the player number, else return 0"""
        # check rows
        for row in self.board:
            for i in range(5):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != 0:
                    return row[i]
        
        # check columns
        for column in range(7):
            for row in range(4):
                if self.board[row][column] == self.board[row+1][column] == self.board[row+2][column] == self.board[row+3][column] != 0:
                    return self.board[row][column]
        
        # check diagonals
        for row in range(4):
            for column in range(5):
                if self.board[row][column] == self.board[row+1][column+1] == self.board[row+2][column+2] == self.board[row+3][column+3] != 0:
                    return self.board[row][column]
        
        return 0    # return 0 if there is no winner
            
    def print_board(self):
        print('-'*25)
        for row in self.board:
            for element in row:
                print(element, end='  ')
            print()
    

    def play(self):
        self.print_board()
        turn = 1
        winner = 0      # no winner initially.
        while winner == 0:    # while there is no winner, keep playing
            usr_input = input('Enter a column number to drop your piece: ')
            self.make_move(turn, int(usr_input))
            winner = self.check_win()
            turn = 2 if turn == 1 else 1
            self.print_board()
        print(f"Player {winner} wins!")
        

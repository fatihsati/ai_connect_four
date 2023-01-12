

class game_operations:

    def make_move(self, board, player, column):
        temp_board = [row[:] for row in board]
        for i in range(6, -1, -1):  # start checking from the bottom, if the column is not full, drop the piece there
            if temp_board[i][column] == 0:
                temp_board[i][column] = player
                return temp_board, True     # return temp_board if the move is successful
        return board, False        # return False if the move is not successful, which means the column is full
    
    def get_possible_moves(self, board):
        possible_moves = [idx  for idx, val in enumerate(board[0]) if val == 0]
        return possible_moves       # return a list which contains the indices of the columns that are not full
        
    def check_win(self, board):
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

        # check tie
        if 0 not in board[0]: return 0 # if al
        return None    # return NOne if game has not finished.
from game_operations import game_operations


class ai:

    def __init__(self):
        self.game_ops = game_operations()


    def get_heuristic_func(self, heuristic_input):
        if heuristic_input == '1':
            return self.h1

    def minimax(self, board, maximizing, heuristic, plyr, depth=0):
        
        opponent = 2 if plyr == 1 else 1
        # get heuristic
        # if 1, return 1
        # if 2, return -1
        # if 0 return 0
        case = self.evaluation(board)
        if case == 1:   # plyr 1 wins
            return 100, None
        if case == 2:   # plyr 2 wins
            return -100, None
        if case == 0:   # tie
            return 50, None

        if depth == 4:
            return heuristic(board, plyr, opponent), None
        
        # if game is not finished yet

        if maximizing:
            max_eval = -1000
            best_move = None
            posbbile_moves = self.game_ops.get_possible_moves(board)
            for column in posbbile_moves:
                temp_board, status = self.game_ops.make_move(board, plyr, column)
                eval = self.minimax(temp_board, False, heuristic, plyr, depth+1)[0]

                if eval > max_eval:
                    max_eval = eval
                    best_move = column
                    
            return max_eval, best_move
    
        if not maximizing:
            min_eval = 1000
            best_move = None
            
            posbbile_moves = self.game_ops.get_possible_moves(board)
            for column in  posbbile_moves:
                temp_board, status = self.game_ops.make_move(board, opponent, column)
                eval = self.minimax(temp_board, True, heuristic, opponent, depth+1)[0]

                if eval < min_eval:
                    min_eval = eval
                    best_move = column
                    
            return min_eval, best_move


    def evaluation(self, board):
        # return 1 if plyr 1 wins,
        # return 2 if plyr 2 wins
        # else return 0
        return self.game_ops.check_win(board)

    def h1(self, board, plyr, opponent):
        # return possible "4 in a row" for plyr
        # count horizontal possibilities
        possibilities_dict = {}
        plyers = [plyr, opponent]
        for turn in plyers:
            possibilities = 0
            for row in board:
                for i in range(5):
                    # count horizontal possible 4 in a row, for plyr. plyr can place a tile if it is 0
                    if row[i] == 0 or row[i] == turn:
                        if row[i+1] == 0 or row[i+1] == turn:
                            if row[i+2] == 0 or row[i+2] == turn:
                                if row[i+3] == 0 or row[i+3] == turn:
                                    possibilities += 1

            for col in range(8):  # each column
                for row in range(4): # each row
                    if board[row][col] == 0 or board[row][col] == turn:
                        if board[row+1][col] == 0 or board[row+1][col] == turn:
                            if board[row+2][col] == 0 or board[row+2][col] == turn:
                                if board[row+3][col] == 0 or board[row+3][col] == turn:
                                    possibilities += 1

            # check diagonals
            for row in range(4):
                for column in range(5):
                    if board[row][column] == 0 or board[row][column] == turn:
                        if board[row+1][column+1] == 0 or board[row+1][column+1] == turn:
                            if board[row+2][column+2] == 0 or board[row+2][column+2] == turn:
                                if board[row+3][column+3] == 0 or board[row+3][column+3] == turn:
                                    possibilities += 1

            # diagonal from right to left
            for row in range(4):
                for column in range(7, 2, -1):  # to check from right to left
                    if board[row][column] == 0 or board[row][column] == turn:
                        if board[row+1][column-1] == 0 or board[row+1][column-1] == turn:
                            if board[row+2][column-2] == 0 or board[row+2][column-2] == turn:
                                if board[row+3][column-3] == 0 or board[row+3][column-3] == turn:
                                    possibilities += 1

            possibilities_dict[turn] = possibilities

        heuristic_value = possibilities_dict[plyr] - possibilities_dict[opponent]
        return heuristic_value

        
    
    # def h2(self, board, plyr, opponent):

        

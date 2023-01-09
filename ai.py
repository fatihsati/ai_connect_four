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
            return 1, None
        if case == 2:   # plyr 2 wins
            return -1, None
        if case == 0:   # tie
            return 0, None

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
        # if there is 2 next to each other that has 2 space next to it, return 1

        # check horizontal
        for row in range(5):
            for column in range(4):
                if board[row][column] == board[row][column + 1] and board[row][column + 2] == board[row][column + 3]:
                    if board[row][column] == plyr and board[row][column + 2] == 0:
                        return 1
                    if board[row][column] == opponent and board[row][column + 2] == 0:
                        return -1
        return 0
    
    # def h2(self, board, plyr, opponent):

        

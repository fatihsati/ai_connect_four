from game_operations import game_operations
import config as cfg

class ai:

    def __init__(self, ai_number, heuristic_number):
        self.game_ops = game_operations()  # create game operations object
        self.ai_number = ai_number # 1 or 2
        self.heuristic = self.get_heuristic_func(heuristic_number) # get heuristic function
        self.opponent_number= 2 if ai_number == 1 else 1 # get opponent number
        

    def get_heuristic_func(self, heuristic_input): # get heuristic function
        if heuristic_input == '1': # h1
            return self.h1
        elif heuristic_input == '2': # h2
            return self.h2
        elif heuristic_input == '3': # h3
            return self.h3

    def minimax(self, board, maximizing, plyr, alpha, beta, depth=0):
        
        opponent = 2 if plyr == 1 else 1
        # get heuristic
        # if 1, return 1
        # if 2, return -1
        # if 0 return 0
        case = self.utility(board)
        if case == self.ai_number:   # plyr 1 wins
            return cfg.utility_win, None

        if case == self.opponent_number:   # plyr 2 wins
            return cfg.utility_lose, None
        if case == 0:   # tie
            return cfg.utility_tie, None

        if depth == cfg.depth:  # 4680 nodes are expanding for the first move with depth = 4
            evalutaion =  self.heuristic(board), None # calculate the evaluation value according to heuristic function
            # print(evalutaion[0])
            return evalutaion # return the evaluation value
        # if game is not finished yet

        if maximizing:
            max_eval = cfg.minimax_max_eval 
            best_move = None
            posbbile_moves = self.game_ops.get_possible_moves(board)
            for column in posbbile_moves:
                temp_board, _ = self.game_ops.make_move(board, plyr, column)
                eval, _ = self.minimax(temp_board, False, plyr, alpha, beta, depth+1)
                if eval >= max_eval:
                    max_eval = eval
                    best_move = column
                
                if max_eval > beta:
                    break   # prune
                alpha = max(alpha, max_eval)

            return max_eval, best_move
    
        if not maximizing:
            min_eval = cfg.minimax_min_eval
            best_move = None
            
            posbbile_moves = self.game_ops.get_possible_moves(board)
            for column in  posbbile_moves:
                temp_board, _ = self.game_ops.make_move(board, opponent, column)
                eval, _ = self.minimax(temp_board, True, opponent, alpha, beta, depth+1)
                min_eval = min(min_eval, eval)
                
                if eval <= min_eval:
                    min_eval = eval
                    best_move = column

                if min_eval < alpha:
                    break   # prune
                beta = min(beta, min_eval)
                
                    
            return min_eval, best_move


    def utility(self, board):
        # return 1 if plyr 1 wins,
        # return 2 if plyr 2 wins
        # else return 0
        return self.game_ops.check_win(board) # check if there is a winner

    def h1(self, board):
        # count three in a row for plyr and opponent, return difference
        plyres = [self.ai_number, self.opponent_number]
        counts = {} # initilize a dictionary for saving counts
        for turn in plyres: # iterate through players
            
            count = 0 # initialize count
            # horizontal
            for row in board:
                for i in range(6):
                    if row[i] == row[i+1] == row[i+2] == turn:
                        count += 1
            # vertical
            for col in range(8):
                for row in range(5):
                    if board[row][col] == board[row+1][col] == board[row+2][col] == turn:
                        count += 1
            # diagonal from left to right
            for row in range(5):
                for col in range(6):
                    if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == turn:
                        count += 1
            # diagonal from right to left
            for row in range(5):
                for col in range(7, 1, -1):
                    if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == turn:
                        count += 1
            
            counts[turn] = count
        heuristic_value = counts[self.ai_number] - counts[self.opponent_number]

        return heuristic_value
            
    def h2(self, board):
        # return difference between possible "4 in a row" for plyr and opponent
        
        # key is the player number, value is the possibilities
        possibilities_dict = {} # number of possibile 4 in a row for each plyr, 
        
        plyers = [self.ai_number, self.opponent_number]
        for turn in plyers:
            possibilities = 0
            
            # count horizontal possibilities
            for row in board:
                for i in range(5):
                    # count horizontal possible 4 in a row, for plyr. plyr can place a tile if it is 0
                    if row[i] == 0 or row[i] == turn:
                        if row[i+1] == 0 or row[i+1] == turn:
                            if row[i+2] == 0 or row[i+2] == turn:
                                if row[i+3] == 0 or row[i+3] == turn:
                                    possibilities += 1
                                    
            # count vertical possibilities
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

            possibilities_dict[turn] = possibilities        # save the possibilities for each plyr

        # print(possibilities_dict)
        # get the evaluation value by subtracting the possibilities of opponent from plyr
        heuristic_value = possibilities_dict[self.ai_number] - possibilities_dict[self.opponent_number]

        return heuristic_value

    def award_func(self, possible_moves, turn, possibilities):
        for possibility in possible_moves: # for each possible sub-board with 4 places
                a = possibility.count(turn) # count the number of tiles of plyr
                b = possibility.count(0) # count the number of empty places
                # award points for each possible 4 in a row
                if a == 3 and b == 1:   # 3 tiles of plyr and 1 empty place
                    possibilities += 100 # award 100 points
                elif a == 2 and b == 2: # 2 tiles of plyr and 2 empty places
                    possibilities += 10 # award 10 points
                elif a == 1 and b == 3: # 1 tile of plyr and 3 empty places
                    possibilities += 1 # award 1 point
        return possibilities # return the total number of award 4 in a row

    def h3(self, board):
        possibilities_dict = {} # number of possibile 4 in each direction for each plyr, 
        plyers = [self.ai_number, self.opponent_number] # list of plyrs

        for turn in plyers: # for each plyr
             
            possibilities = 0 # initialize the number of possibilities to 0
            # count horizontal possibilities
            horizontal_possibilities = [] # list of possible 4 in a row in horizontal direction
            for row in board: # for each row
                for i in range(5): 
                    # count horizontal possible 4 in a row, for plyr. plyr can place a tile if it is 0
                    horizontal_possibilities.append([row[i], row[i+1], row[i+2], row[i+3]])
            possibilities = self.award_func(horizontal_possibilities, turn, possibilities) # award points for each possible 4 in a row
            # count vertical possibilities
            vertical_possibilities = [] # list of possible 4 in a row in vertical direction
            for col in range(8):  # each column
                for row in range(4): # each row
                    vertical_possibilities.append([board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]]) # append the 4 places in a column
            
            possibilities = self.award_func(vertical_possibilities, turn, possibilities) # award points for each possible 4 in a row
                
            # check diagonals
            diagonal_possibilities = [] # list of possible 4 in a row in diagonal direction
            for row in range(4): # for each row
                for column in range(5): # for each column
                    diagonal_possibilities.append([board[row][column], board[row+1][column+1], board[row+2][column+2], board[row+3][column+3]]) # append the 4 places in a diagonal

            possibilities = self.award_func(diagonal_possibilities, turn, possibilities) # award points for each possible 4 in a row
            # diagonal from right to left
            inverse_diagonal_possibilities = [] # list of possible 4 in a row in inverse diagonal direction
            for row in range(4): # for each row
                for column in range(7, 2, -1):  # to check from right to left
                    inverse_diagonal_possibilities.append([board[row][column], board[row+1][column-1], board[row+2][column-2], board[row+3][column-3]]) # append the 4 places in a diagonal
            
            possibilities = self.award_func(inverse_diagonal_possibilities, turn, possibilities) # award points for each possible 4 in a row
            possibilities_dict[turn] = possibilities       # save the possibilities for each plyr
        heuristic_value = possibilities_dict[self.ai_number] - possibilities_dict[self.opponent_number] # calcuate the heuristic value for the current player
        return heuristic_value 

        

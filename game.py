from ai import ai
from game_operations import game_operations
import config as cfg

class Game:
    """All functions related with the game will be defined here,
        including the board, the moves, the win conditions, etc.
        """
    def __init__(self):
        self.game_ops = game_operations() # create game_operations object

    def initilize_board(self):
        board = [[0 for i in range(8)] for j in range(7)] # create 7x8 board
        return board # return the board

    def print_board(self, board):  
        for row in board:
            for element in row: # print each element in the row
                if element == 0: # if element is 0, print '-'
                    print('-', end='  ')
                    continue
                print(element, end='  ') # print the element
            print()
        print('-'*25) # print a line to separate the board from the next move

    def two_player_game(self): # two player game
        print() # print empty line 
        board = self.initilize_board() # initialize the board
        self.print_board(board) # print the board
        turn = 1 # player 1 starts
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            usr_input = input('Enter a column number to drop your piece: ') # ask for input
            board, status = self.game_ops.make_move(board, turn, int(usr_input)) # make the move
            if not status:
                print('invalid input, try again') # if the move is invalid, ask for input again
                continue
            winner = self.game_ops.check_win(board) # check if there is a winner
            turn = 2 if turn == 1 else 1 # change the turn
            self.print_board(board) # print the board
        print(f"Player {winner} wins!") # print the winner


    def one_player_game(self): # one player game
        
        heuristic_number = input('Select heuristic number between 1-3: ') # ask for heuristic number
        ai_1 = ai(1, heuristic_number) # create ai object
        print() # print empty line
            
        board = self.initilize_board() # initialize the board
        self.print_board(board) # print the board
        turn = 1 # player 1 starts
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # ai
                eval, move = ai_1.minimax(board, True, turn, cfg.alpha, cfg.beta) # get the move from the ai
                board, status = self.game_ops.make_move(board, turn, move) # make the move
                print('AI move:', move, 'eval', eval) # print the move and the evaluation

            else:   # plyr
                usr_input = input('Enter a column number to drop your piece: ') # ask for input from the human player
                board, status = self.game_ops.make_move(board, turn, int(usr_input)) # make the move
                if not status: # if the move is invalid, ask for input again
                    print('invalid input, try again')
                    continue

            winner = self.game_ops.check_win(board) # check if there is a winner
            turn = 2 if turn == 1 else 1 # change the turn
            self.print_board(board) # print the board
        print(f"Player {winner} wins!") # print the winner
    
    def ai_vs_ai(self):
        
        heuristic_number1 = input('Select heuristic number between 1-3 (AI 1): ') # ask for heuristic number for AI 1
        heuristic_number2 = input('Select heuristic number between 1-3 (AI 2): ') # ask for heuristic number for AI 2
        ai_1 = ai(1, heuristic_number1) # create first ai object with the given heuristic number
        ai_2 = ai(2, heuristic_number2) # create second ai object with the given heuristic number
        print() # print empty line
        
        board = self.initilize_board() # initialize the board
        self.print_board(board) # print the board
        turn = 1 # player 1 starts
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # AI 1
                eval, move = ai_1.minimax(board, True, turn, cfg.alpha, cfg.beta) # get the move from the AI 1
                board, status = self.game_ops.make_move(board, turn, move) # make the move
                print('AI 1 move:', move, 'eval: ', eval)

            else:   # AI 2
                eval, move = ai_2.minimax(board, True, turn, cfg.alpha, cfg.beta) # get the move from the AI 2
                board, status = self.game_ops.make_move(board, turn, move) # make the move
                print('AI 2 move:', move, 'eval: ', eval)

            winner = self.game_ops.check_win(board) # check if there is a winner
            turn = 2 if turn == 1 else 1 # change the turn
            self.print_board(board) # print the board

        print(f"Player {winner} wins!") # print the winner

    def play(self):
        game_type = input("1.Two Player\n2.1vsAI\n3.AI1 vs AI2\nSelect game mode: ") # ask for game mode
        if game_type == '1': 
            self.two_player_game() 
        
        elif game_type == '2':
            self.one_player_game()
        
        elif game_type == '3':
            self.ai_vs_ai()
        else:
            print('invalid input')
            self.play()

game = Game()
game.play()
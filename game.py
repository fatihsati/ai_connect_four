from ai import ai
from game_operations import game_operations
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
        self.ai = ai()
        self.game_ops = game_operations()

    def initilize_board(self):
        board = [[0 for i in range(8)] for j in range(7)]
        return board

    def print_board(self, board):
        print('-'*25)
        for row in board:
            for element in row:
                print(element, end='  ')
            print()


    def two_player_game(self):
        board = self.initilize_board()
        self.print_board(board)
        turn = 1
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            usr_input = input('Enter a column number to drop your piece: ')
            board, status = self.game_ops.make_move(board, turn, int(usr_input))
            if not status:
                print('invalid input, try again')
                continue
            winner = self.game_ops.check_win(board)
            turn = 2 if turn == 1 else 1
            self.print_board(board)
        print(f"Player {winner} wins!")


    def one_player_game(self):
        heuristic_number = input('Select heuristic number between 1-3: ')
        heuristic_function = self.ai.get_heuristic_func(heuristic_number)

            
        board = self.initilize_board()
        self.print_board(board)
        turn = 1
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # ai
                eval, move = self.ai.minimax(board, True, heuristic_function, turn)
                board, status = self.game_ops.make_move(board, turn, move)
            else:   # plyr
                usr_input = input('Enter a column number to drop your piece: ')
                board, status = self.game_ops.make_move(board, turn, int(usr_input))
                if not status:
                    print('invalid input, try again')
                    continue

            winner = self.game_ops.check_win(board)
            turn = 2 if turn == 1 else 1
            self.print_board(board)
        print(f"Player {winner} wins!")
    
    def ai_vs_ai(self):
        heuristic_number1 = input('Select heuristic number between 1-3 (AI 1): ')
        heuristic_number2 = input('Select heuristic number between 1-3 (AI 2): ')
        heuristic_function1 = self.ai.get_heuristic_func(heuristic_number1)
        heuristic_function2 = self.ai.get_heuristic_func(heuristic_number2)

        board = self.initilize_board()
        self.print_board(board)
        turn = 1
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # AI 1
                eval, move = self.ai.minimax(board, True, heuristic_function1, turn)
                board, status = self.game_ops.make_move(board, turn, move)
            else:   # AI 2
                eval, move = self.ai.minimax(board, True, heuristic_function2, turn)
                board, status = self.game_ops.make_move(board, turn, move)

            winner = self.game_ops.check_win(board)
            turn = 2 if turn == 1 else 1
            self.print_board(board)
        print(f"Player {winner} wins!")

    def play(self):
        game_type = input("Select game mode:\n1.Two Player\n2.1vsAI\n3.AI1 vs AI2\n")
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
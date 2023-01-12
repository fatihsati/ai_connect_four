from ai import ai
from game_operations import game_operations
import config as cfg

class Game:
    """All functions related with the game will be defined here,
        including the board, the moves, the win conditions, etc.
        """
    def __init__(self):
        self.game_ops = game_operations()

    def initilize_board(self):
        board = [[0 for i in range(8)] for j in range(7)]
        return board

    def print_board(self, board):  
        for row in board:
            for element in row:
                if element == 0:
                    print('-', end='  ')
                    continue
                print(element, end='  ')
            print()
        print('-'*25)

    def two_player_game(self):
        print() # print empty line
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
        ai_1 = ai(1, heuristic_number)
        print() # print empty line
            
        board = self.initilize_board()
        self.print_board(board)
        turn = 1
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # ai
                eval, move = ai_1.minimax(board, True, turn, cfg.alpha, cfg.beta)
                board, status = self.game_ops.make_move(board, turn, move)
                print('AI move:', move, 'eval', eval)

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
        ai_1 = ai(1, heuristic_number1)
        ai_2 = ai(2, heuristic_number2)
        print() # print empty line
        
        board = self.initilize_board()
        self.print_board(board)
        turn = 1
        winner = None      # no winner initially.
        while winner == None:    # while there is no winner, keep playing
            if turn == 1:   # AI 1
                eval, move = ai_1.minimax(board, True, turn, cfg.alpha, cfg.beta)
                board, status = self.game_ops.make_move(board, turn, move)
                print('AI 1 move:', move, 'eval: ', eval)

            else:   # AI 2
                eval, move = ai_2.minimax(board, True, turn, cfg.alpha, cfg.beta)
                board, status = self.game_ops.make_move(board, turn, move)
                print('AI 2 move:', move, 'eval: ', eval)

            winner = self.game_ops.check_win(board)
            turn = 2 if turn == 1 else 1
            self.print_board(board)

        print(f"Player {winner} wins!")

    def play(self):
        game_type = input("1.Two Player\n2.1vsAI\n3.AI1 vs AI2\nSelect game mode: ")
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
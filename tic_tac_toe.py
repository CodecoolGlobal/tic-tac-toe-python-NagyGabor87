from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
# from function5 import get_umbeatable_ai_coordinates
from function6 import get_winning_player
from function7 import is_board_full
import time


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    turn = 0
    is_game_running = True
    while is_game_running:
        display_board(board)

        if game_mode == "1":
            current_player = 'X'
            turn += 1
            if turn % 2 == 0:
                current_player = 'O'
            else:
                current_player = 'X'
            x, y = get_human_coordinates(board, current_player)
            board[x][y] = current_player
            is_game_running = board_check(board)

        if game_mode == "2":
            current_player = 'X'
            x, y = get_random_ai_coordinates(board, current_player)
            is_game_running = board_check(board)
            board[x][y] = current_player
            time.sleep(2)
            x, y = get_random_ai_coordinates(board, current_player)
            is_game_running = board_check(board)
            board[x][y] = 'O'

        if game_mode == "3":
            current_player = 'X'
            x, y = get_human_coordinates(board, current_player)
            is_game_running = board_check(board)
            board[x][y] = current_player
            x, y = get_random_ai_coordinates(board, current_player)
            is_game_running = board_check(board)
            board[x][y] = 'O'


def board_check(board):

    winning_player = get_winning_player(board)
    its_a_tie = is_board_full(board)
    if winning_player == 'X':
        display_board(board)
        print('X won the game')
        return False

    elif winning_player == 'O':
        display_board(board)
        print('O won the game')
        return False

    elif not winning_player and its_a_tie:
        display_board(board)
        print("It's a tie")
        return False
    return True


if __name__ == "__main__":
    main()

# TO DO ###
# based on the values of `winning_player` and `its_a_tie` the program
# should either stop displaying a winning/tie message
# OR continue the while loop

# TO DO ###
# based on the value of the variables `game_mode` and `current_player`
# the programm should should choose betwen the functions
# get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinate

# TO DO ###
# in each new iteration of the while loop the program should
# alternate the value of `current_player` from `X` to `O`

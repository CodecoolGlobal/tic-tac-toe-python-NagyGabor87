def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append('.')
        board.append(row)
    return board
        



if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = get_empty_board()
    print(board)

get_empty_board()

def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''
    row1 = ['.', '.', '.']
    row2 = ['.', '.', '.']
    row3 = ['.', '.', '.']
    board = []
    board.append(row1)
    board.append(row2)
    board.append(row3)
    return board
    pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = get_empty_board()
    print(board)

get_empty_board()

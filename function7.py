def is_board_full(board):
  """
  should return True if there are no more empty place on the board,
  otherwise should return False
  """
  for row in board:
    for item in row:
      if item == ".":
        return False
  return True


# vagy lehetne:

def is_board_full(board):
  for row in range(len(board)):
    for item in range(len(board)):
      if board[row][item] == ".":
        return False
  return True


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(is_board_full(board_1)) # should return False

  board_2 = [
    [".", "O", "O"],
    [".", "O", "X"],
    [".", "X", "X"],
  ]
  print(is_board_full(board_2)) # should return False

  board_3 = [
    ["O", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"],
  ]
  print(is_board_full(board_3)) # should return True
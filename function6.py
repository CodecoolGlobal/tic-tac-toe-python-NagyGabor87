def get_winning_player(board):
  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  b = True
  while b:
    player_symbols = ("X","O")
    for player in player_symbols: 
      for row in board:
        if row[0] == row[1] == row[2] == player:
          return player

      for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
          return player
      
      if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return player
    else:
      return None  
  




if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_winning_player(board_1)) # should return "X"

  board_2 = [
    ["X", "O", "O"],
    ["X", "O", "."],
    ["O", "X", "X"],
  ]
  print(get_winning_player(board_2)) # should return "O"

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_winning_player(board_3)) # should return None
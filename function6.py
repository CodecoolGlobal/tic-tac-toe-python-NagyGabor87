

def get_winning_player(board):
  """
  Should return the player that wins based on the tic tac toe rules.
  If no player has won, than "None" is returned.
  """
  b = True
  while b:
    player_symbols = ("X","O")
    for player in player_symbols: 
      for row in board:  # sorokért megy be a boardba, és a sor elemeit nézi meg, hogy megegyeznek-e
        if row[0] == row[1] == row[2] == player:
          return player

      for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] == player:
          return player

      if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return player
    else:
      return None





if __name__ == "__main__":  # minden fájlnak van egy __name__-e ami a saját fájlneve és ami örök, amikor importálsz
# valamit, akkor a __name__ az importált fájl nevéről nyilván az adott fájl neve lesz amit futtatsz, nem amiből
# futtatja le a dolgokat ,így amikor leírod, a fájlban (ahova akár importáltál dolgokat),
# hogy a __name__-ed a __main__re mutat (ami az adott fájl neve maga), akkor azt ami az alatt van
# csak akkor futtatja le, amikor azt a fájlt futtatod, ha máshova átimportálod értelemszerűen a __name__
# megváltozik, így nem fog teljesülni az if és nem fut le
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
from get_winning_player import get_winning_player
from is_board_full import is_board_full

def get_unbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """

  bestScore = -1000
  bestMove = (-1,-1)

  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == ".":
        board[i][j] = current_player
        score = minimax(board, 0, False, current_player)
        board[i][j] = "."
        if (score > bestScore):
          bestScore = score
          bestMove = (i, j)

  return bestMove

def evaluate(board, current_player, opponent) : 
  player = get_winning_player(board)
  if player == current_player:
     return 10
  elif player == opponent:
     return -10
  else:
     return 0


def minimax(board, depth, isMaximizing, current_player):
  if current_player == "X":
       opponent = "O"

  elif current_player == "O":
       opponent = "X"

  score = evaluate(board, current_player, opponent)

  if (score == 10) : 
        return score
  
  if (score == -10) :
        return score
  
  if (is_board_full(board) == True) :
        return 0

  if isMaximizing:
      bestScore = -1000
      for i in range(len(board)):
        for j in range(len(board)):
          if board[i][j] == ".":
            board[i][j] = current_player
            bestScore = max(bestScore, minimax(board, depth + 1, not isMaximizing, opponent) )
            board[i][j] = "."
      return bestScore
  else:
    bestScore = 1000
    for i in range(len(board)):
        for j in range(len(board)):
          if board[i][j] == ".":
            board[i][j] = opponent
            bestScore = min(bestScore, minimax(board, depth + 1, not isMaximizing, current_player))
            board[i][j] = "."
    return bestScore


  

if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_unbeatable_ai_coordinates(board_1, "X")) # the printed coordinate should always be (0, 0)
  

  board_2 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print(get_unbeatable_ai_coordinates(board_2, "O")) # the printed coordinate should always be (1, 1)
  

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_unbeatable_ai_coordinates(board_3, "X")) # the printed coordinate should be either (0, 2) or (2, 0)
 
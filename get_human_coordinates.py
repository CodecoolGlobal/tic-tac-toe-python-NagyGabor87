

def get_human_coordinates(board, player_input):
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  then a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  then a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  found = False
  while not found:
    player_input = input("Choose a coordinate (for example: A2, C1): ").upper()
    valid_input = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    if player_input == "QUIT":
      quit()
    player_coord_input = []
    if player_input in valid_input:
      player_coord_input = [(player_input[:1]), int(player_input[1:])]
      row = 0
      col = 0
      match player_coord_input[0]:
        case "A":
          row = 0
        case "B":
          row = 1
        case "C":
          row = 2
      match player_coord_input[1]:
        case 1:
          col = 0
        case 2:
          col = 1
        case 3:
          col = 2        
      coordinates = (row,col)
    else:
      print("Invalid coordinate")
      continue

    if board[coordinates[0]][coordinates[1]] != ".":
      print("The coordinate is already taken")
      continue
    found = True

  return coordinates





if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones


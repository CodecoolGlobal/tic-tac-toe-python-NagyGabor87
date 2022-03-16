

def get_human_coordinates(board, current_player):
  """
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """
  player_input = input("Choose a coordinate (for example: A2, C1): ").upper()
  valid_input = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
  if player_input == "QUIT":
    quit()
  player_coord_input = [(player_input[:1]), int(player_input[1:])]   
  if player_input in valid_input:
    if player_coord_input[0] == "A":
      player_coord_input[0] = 0
    elif player_coord_input[0] == "B":
      player_coord_input[0] = 1
    elif player_coord_input[0] == "C":
      player_coord_input[0] = 2
    if player_coord_input[1] == 1:
      player_coord_input[1] = 0
    elif player_coord_input[1] == 2:
      player_coord_input[1] = 1
    elif player_coord_input[1] == 3:
      player_coord_input[1] = 2
    player_coord_input = tuple(player_coord_input)
    already_tried_coord = []
    already_tried_coord.append(player_coord_input)
    if player_coord_input is current_player:
      print("Coordinate is already taken")
  else:
    print("Invalid coordinate")


  # if player_coord_input in valid_input:
  # player_coord_input.format(0)
  print(player_coord_input)
  # if player_input in valid_input:
  l = []
  for i in range(len(board)):
    for j in range(len(board)):
      if board[i][j] == ".":
        l.append((i,j))
  return l



if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones

# new_list = [0, 1, 2]
# new_tuple = ["A", "B", "C"]
# new_tuple.index(new_tuple, len(new_list))
# for n in new_list:
#   new_list.append(new_tuple[n])
# print(new_tuple)
# for i in new_list:
#   element = str(new_list[0], [1], [2]) + new_tuple[0], [1], [2]
# print(element)
  # new = get_human_coordinates(board_1, 0)
  # board_1[new[0]] [new[1]] = 'X'
  # print(board_1)
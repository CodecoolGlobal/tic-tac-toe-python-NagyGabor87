def display_board(board):
  """
  Should print the tic tac toe board in a format similar to
       1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | . 
       --+---+---
  """
  
print("\n")
print(f'    1      2      3' )
print("\n")
print(f'A  "." |  "." |  "."')
print(f'  -----+------+-----')
print(f'B  "." |  "." |  "."')
print(f'  -----+------+-----')
print(f'C  "." |  "." |  "."')
print(f'  -----+------+-----')


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ['X', "O", "."],
      ['X', "O", "."],
      ['0', "X", "."]
    ]
    display_board(board)
    # should print 
    #     1   2   3
    # A   X | O | . 
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | . 
    #    --+---+---


print(display_board(board))

list = []
for r in range(3):
   list.append([])
   for c in range(3):
      list[r].append('.')

print(list)

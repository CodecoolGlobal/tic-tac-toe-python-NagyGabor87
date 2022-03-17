

def display_board(board):
   print(f'\n     1.       2.       3.  \n')

   for row, row_index in zip(board, ("A", "B", "C")):
      print(f'{row_index}    {row[0]}   |    {row[1]}    |   {row[2]}   | ')
      print(f'  - - - - - - - - - - - - - ')


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


# list = []
# for r in range(3):
#    list.append([])
#    for c in range(3):
#       list[r].append('.')

# print(list)

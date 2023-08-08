def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  print('''
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI''')
  correct_input = ['1', '2', '3', '4']
  b = True
  while b:
    player_option = input("Choose from the options above: ")
    if player_option in correct_input:
      b = False
    else:
      print("Input a new value")
  return player_option


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1


print(get_menu_option)

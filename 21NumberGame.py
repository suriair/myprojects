num_list = []

print('Player 2 is Computer.\n')

nod = input('Do you want to start the game? (Yes/No)\n')

  
if nod == 'Yes' or nod == 'yes':
  print('\n')
  query = input("Enter 'F' to take the first chance.\nEnter 'S' to take the second chance.\n")

def player_human(): 
  i = 0
  while i >= 0:
    print('\n')
    num_wish = int(input('How many numbers do you wish to enter?\n'))
    print('\n')
    global num_enter
    num_enter = input('Enter your values:\n')
    num_enter = num_enter.split(',')
    num_enter = [int(x) for x in num_enter]
    if len(num_enter) == num_wish:
      num_list.extend(num_enter)
      break
    else:
      print('\n')
      print("'Number Entered' is not equal to 'Number Wished' to enter.")
      i += 1

def player_comp():
  print('\n')
  if len(num_list) == 0:
    num_list.append(1)
    print(f"Order of input after Computer's turn is: {num_list}")
  else:
    to_appnd = [len(num_list) + 1, len(num_list) + 2, len(num_list) + 3]
    num_list.extend(to_appnd)
    print(f"Order of input after Computer's turn is: {num_list}")
    
if query == 'F' or query == 'f':
  while True:
    player_human()
    if len(num_list) == 20 and 20 in num_enter:
      print('\nYOU WON !!!')
      break
    elif len(num_list) > 20:
      print('\nYOU LOSE !!!')
      break
    player_comp()
    if len(num_list) > 20:
      print('\nYOU WON !!!')
      break
    elif len(num_list) == 20:
      print('\nYOU LOSE !!!')
      break
    else:
      print('\nYour Turn.')
      
elif query == 'S' or query == 's':
  while True:
    player_comp()
    if len(num_list) > 20:
      print('\nYOU WON !!!')
      break
    elif len(num_list) == 20:
      print('\nYOU LOSE !!!')
      break
    else:
      print('\nYour Turn.')
    player_human()
    if len(num_list) == 20 and 20 in num_enter:
      print('\nYOU WON !!!')
      break
    elif len(num_list) > 20:
      print('\nYOU LOSE !!!')
      break
  
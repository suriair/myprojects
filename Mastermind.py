import random

random_number = random.randint(1000,10000)
random_number = str(random_number)
correct_digit = ['_' for r in random_number]

print('NOTE: You are playing against Computer.')

guess_number = input(f'\nPlayer, Guess the {len(random_number)} digit number: ')

if random_number == guess_number:
  print("\nGreat! You guessed the number in just 1 try! You're a Mastermind!")
else:
  x = 1
  while x >=1:
    for i in range(len(random_number)):
      if guess_number[i] == random_number[i]:
        correct_digit[i] = guess_number[i]
      elif guess_number[i] != random_number[i]:
        correct_digit[i] = 'x'
    x +=1
    y = int(len(random_number)) - int(correct_digit.count('x'))
    if y == 0:
      print('\nNot quite the number. Try Again !')
    else:
      print(f'\nNot quite the number. You did get {y} digit(s) correct.')
    for n in correct_digit:
      print(n,end=' ')
    guess_number = input('\nEnter your next choice of numbers: ')
    if random_number == guess_number:
      print("You've become a Mastermind.")
      print(f"It took you only {x} tries.")
      break
    
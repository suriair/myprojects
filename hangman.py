import random

fruit_name = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

fruit_name = fruit_name.split(' ')

def other_letter_guess(input_given, ran_fruit):
  guess = 0
  while guess < len(ran_fruit) + 2:
    print('\n')
    input_given = input('Enter the fruit name: ')
    if input_given == ran_fruit:
      print('\n')
      print('Yeah ! you guessed it right.')
      break
    else:
      print('\n')
      print('Oops ! Try Again')
      guess +=1
  else:
    print('\n')
    print('OUT OF GUESSES !!!')


def random_fruits(fruit_name):
  global ran_fruit
  ran_fruit = random.choice(fruit_name)
  i = 0
  while i >= 0:
    global input_given 
    input_given = input('Enter a letter: ')
    if input_given in ran_fruit:
      print('\n')
      print(f'The length of the fruit word is: {len(ran_fruit)}')
      position_letter = 1 + ran_fruit.find(input_given)
      print(f"The position of '{input_given}' in fruit word is at: {position_letter}")
      print('\n')
      print('Guess the fruit name ???')
      print('\n')
      print('Best of Luck !!!')
      other_letter_guess(input_given, ran_fruit)
      break
    else:
      print('Letter not present in fruit name.')

random_fruits(fruit_name)

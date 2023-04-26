import random

fruit_name = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''

input_save = []

fruit_name = fruit_name.split(' ')

ran_fruit = random.choice(fruit_name)

print('Guess the word! HINT: word is a name of the fruit.\n')

fruit_word = ['_' for i in range(len(ran_fruit))]

for s in fruit_word:
  print('_', end=' ')

print('\n\nENTER ONE CHARACTER AT A TIME.')


guess = 0
while guess < len(ran_fruit) + 2:
  print('\n') 
  input_given = str(input('Enter a letter to guess: '))
  if input_given in ran_fruit:
    input_save.append(input_given)
    for x in range(len(input_save)):
      for y in range(len(fruit_word)):
        if ran_fruit[y] == input_save[x]:
          fruit_word[y] = input_save[x]
    for a in fruit_word:
      print(a,end=' ')
  else:
    print('Oops! No match found!.')
    guess +=1
  if '_' not in fruit_word:
    print('\n\nYOU WON !!!')
    break
else:
  print('You LOSE!')
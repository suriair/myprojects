import random
option = ['rock', 'paper', 'scissor']


user_choice = input('User choice is: ')
computer_choice = random.choice(option)

if user_choice == computer_choice:
	print("It's a Draw." )
elif user_choice == 'rock' and computer_choice == 'paper':
	print('rock V/s paper\npaper wins')





	



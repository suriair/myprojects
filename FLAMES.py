print('Please, Enter your name in lowercase.\n')

player1 = input('player1 name: ')
player2 = input('player2 name: ')

for x in range(len(player1)):
	for y in range(len(player2)):
		if player1[x] == player2[y]:
			player1 = player1.replace(player2[y], ' ', 1)
			player2 = player2.replace(player2[y], ' ', 1)
			
player_concated = player1 + player2
player_concated = player_concated.replace(' ', '')

def loop(player_concated):
	updated_flames = []
	flames = ['f','l','a','m','e','s']
	
	i = 0
	while i < 5:
		count = len(player_concated)
		updated_flames.clear()
		for z in range(len(flames)):
			if z == len(flames) - 1:
				continue
			else:
				index = (count + z) % len(flames)
				updated_flames.append(flames[index])
		flames = updated_flames.copy()
		i +=1
	return flames    	

flames_describe = {'f': 'Friend', 'l': 'Lover', 'a': 'Affectionate', 'm': 'Marriage', 'e': 'Enemies', 's': 'Sibling'}

for key, value in flames_describe.items():
	if key in loop(player_concated):
		print(f'\nRelationship status: {value}')

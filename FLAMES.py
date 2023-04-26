player1 = input('player1 name: ')
player2 = input('player2 name: ')

for x in range(len(player1)):
	for y in range(len(player2)):
		if player1[x] == player2[y]:
			player1 = player1.replace(player2[y], ' ', 1)
			player2 = player2.replace(player2[y], ' ', 1)
			
player_concated = player1 + player2
player_concated = player_concated.replace(' ', '')

flames = ['F','L','A','M','E','S']

def flames_appender(player_concated, flames):
	to_add = len(player_concated) - len(flames)
	for i in range(to_add):
		flames.append(flames[i])

if len(player_concated) > len(flames):
	flames_appender(player_concated, flames)

print(flames)
player1 = input('player1 name: ')
player2 = input('player2 name: ')

for x in range(len(player1)):
	for y in range(len(player2)):
		if player1[x] == player2[y]:
			player1 = player1.replace(player2[y], ' ', 1)
			player2 = player2.replace(player2[y], ' ', 1)
			
player_concated = player1 + player2
player_concated = player_concated.replace(' ', '')

flames = 'flames'

def flames_appender(player_concated):
	global flames
	for i in range(len(player_concated)+2):
		flames = flames + 'flames'

flames_appender(player_concated)

to_replace = flames[4::len(player_concated)]
print(to_replace)

for z in range(len(to_replace)):
	flames = flames.replace(to_replace[z], '')

print(flames)

flames_describe = {'f': 'Friend', 'l': 'Lover', 'a': 'Affectionate', 'm': 'Marriage', 'e': 'Enemies', 's': 'Sibling'}

for key, value in flames_describe.items():
	if key == flames[0]:
		print(value)

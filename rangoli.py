n = int(input("Enter the num of alphabet you want to use for making a rangoli: "))
num_of_lines = 0

for i in range(0,n):
  num_of_lines += 2
  
num_of_lines -= 1
num_of_lines *= 2
num_of_lines -= 1

alpha = 'abcdefghijklmnopqrstuvwxyz'

rangoli = []
alpha_num = 1

for j in range(num_of_lines):
  rangoli.append('-')

while alpha_num < n+1:
  for k in range(0,round(num_of_lines / 2),2):
    rangoli[k] = rangoli[k+2]
    rangoli[-(k+1)] = rangoli[-(k+1)-2]
  rangoli[round(num_of_lines / 2)] = alpha[n-alpha_num]
  alpha_num +=1
  print(''.join(rangoli))

alpha_num_reverse = 1
while alpha_num_reverse < n:
  for x in range(round(num_of_lines / 2)-2,-2,-2):
    rangoli[x] = rangoli[x-2]
    rangoli[x-2] = '-'
    rangoli[-(x+1)] = rangoli[-(x+1)+2]
    rangoli[-(x+1)+2] = '-'
  rangoli[round(num_of_lines / 2)] = alpha[alpha_num_reverse]
  alpha_num_reverse +=1
  print(''.join(rangoli))
  
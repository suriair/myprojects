from PIL import ImageGrab

i = 0
while i >= 0:
	input_given = input("press 'S' to capture the screenshot: ") 
	if input_given == 'S' or input_given == 's':
		screenshot = ImageGrab.grab()
		screenshot.show()
		break
	else:
		print('Invalid input.')
		i +=1
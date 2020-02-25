import sys
def get_move(data):
	board=[[0 for i in range (data['board']['height'])] for i in range(data['board']['width'])]


	for food in data['board']['food']:
		x=food['x'] 
		y=food['y']
		board[x][y]=1

	for x in range(len(board)):
		for y in range(len(board[0])):
			sys.stdout.write(str(board[x][y]))
		sys.stdout.write('\n')



 get_move()
 turn_left()
 get_move()
 turn_left()
 get_move()
 turn_left()
 get_move()
 turn_left()    
 
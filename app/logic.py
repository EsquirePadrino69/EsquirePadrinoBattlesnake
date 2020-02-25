from random import shuffle
def get_move(data):
	food = set()
	for f in data['board']['food']:
		x = f['x']
		y = f['y']
		point = (x, y)
		food.add(point)
	print(food)

	unsafe = set()
	for snake in data['board']['snakes']:
		for p in snake['body']:
			x = p['x']
			y = p['y']
			point = (x, y)
			unsafe.add(point)
	head = data['you']['body'][0]
	x = head['x']
	y = head['y']
	head_left = (x-1, y)
	head_up = (x, y-1)
	head_down = (x, y+1)
	head_right = (x+1, y)
	moves = [("left", head_left), ("up", head_up), ("down", head_down), ("right", head_right)]
	board_height = data['board']['height']
	board_width = data['board']['width']
	shuffle(moves) 
	for move in moves:
		if move[1][0] < 0 or move[1][0] >= board_width:
			continue
		if move[1][1] < 0 or move[1][1] >= board_height:
			continue
		if move[1] in unsafe:
			continue
		return move[0]
	return ":shrug:"

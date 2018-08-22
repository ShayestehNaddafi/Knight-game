from game_objects import Knight, Item
import random 
import sys

def create_board(size):
	board = {}
	for row in range(0, size):
		for col in range(0, size):
			board[(row, col)] = []
	return board

def update_board(board, elements):
	for element in elements:
		if element.position and element not in board[element.position]:
			board[element.position].append(element)
	
def remove_elements_from_board(board, elements):
	for element in elements:
		if element in board[element.position]:
			board[element.position].remove(element)

def get_new_position(position, direction):
	row, col = position
	if direction == 'E':
		new_position = (row, col + 1)
	elif direction == 'S':
		new_position = (row + 1, col)
	elif direction =='N':
		new_position = (row - 1, col)
	elif direction == 'W':
		new_position =	(row, col - 1)
	
	return new_position

def battle_result(attacker, defender):
	if attacker.attack + 0.5 > defender.defence:
		loser = defender
	else:
		loser = attacker
	item = loser.item
	if  item:
		item.release(loser.position)
	loser.died()
	return (attacker, defender, item)	
	
def get_available_items(elements):
	return [el for el in elements if type(el) == Item]

def get_knight(elements):
	for el in elements:
		if type(el) == Knight:
			return el
	return None
	
def is_drown(position):
	row, col = position
	if 0 <= row < 8 and 0 <= col < 8:
		return False
	else:
		return True

def drown_knight(knight):
	item = knight.item
	if item:
		item.release(knight.position)
	knight.drown()
	return item
	
def handle_movement(board, position, knight):
	if is_drown(position):
		remove_elements_from_board(board, [knight])
		item = drown_knight(knight)
		update_board(board, [item])
	else:
		current_elements = board[position]
		items = get_available_items(current_elements)
		defender = get_knight(current_elements)
		remove_elements_from_board(board, [knight])
		knight.update_position(position)	
		if len(items) > 0 and not knight.item:
			item = random.choice(items)
			remove_elements_from_board(board, [item])
			knight.equipped(item)
			
		if defender and defender.is_alive():
			knight, defender, item = battle_result(knight, defender)
			update_board(board, [knight, defender, item])
		else:	
			update_board(board, [knight])

def read_file(file):
	l = []
	with open(file,'r') as f:
		for line in f:
			l.append(line.strip())

	return l 

def get_moves_and_check_content_is_valid(data):	
	moves = []
	msg = 'The input file does not have a correct content'
	if data[0] == 'GAME-START' and data[-1] == 'GAME-END':
		data = data[1:-1]
	else: 
		print(msg)
		sys.exit(0)
	knights = ['R', 'B', 'G', 'Y']
	directions = ['E', 'W', 'N', 'S']
	for movement in data:
		if movement[0] not in knights or movement[2] not in directions:
			print(msg)
			sys.exit(0)
		else:
			moves.append((movement[0], movement[2]))
		 
	return moves

def print_result(knights, items):
	print('{')
	for k in knights:
		it = k.item.name if k.item else None
		print('{}: {},'.format(k.name, [k.position, k.status, it, k.attack, k.defence]))
	for item in items:
		print('{}: {},'.format(item.name, [item.get_position(), item.owner is not None]))
	print('}')

def run_game(input_file):				
	board = create_board(8)
	r = Knight('red', (0,0))
	b = Knight('blue', (7,0))
	g = Knight('green', (7,7))
	y = Knight('yellow', (0,7))
	a = Item('axe', (2,2), 2, 0)
	d = Item('dagger', (2,5), 1, 0)
	h = Item('helmet', (5,5), 1, 0)
	m = Item ('magic_staff', (5,2), 1, 0 )
	knights_dict = {'R': r, 'B': b, 'G': g, 'Y': y}
	knights = [r, b, g, y]
	items = [a, d, h, m]
	update_board(board, knights + items)	
	input_data = read_file(input_file)
	movements = get_moves_and_check_content_is_valid(input_data)
	for knight_name, direction in movements:
		knight = knights_dict[knight_name]
		if knight.is_alive():
			next_position = get_new_position(knight.position, direction)
			handle_movement(board, next_position, knight) 
	return knights, items		

def main():
	knights, items = run_game('./moves2.txt')
	print_result(knights, items)

if __name__ == "__main__":
	main()

import unittest
import knight_game

class TestGame(unittest.TestCase):
	def test_run_game_move(self):
		# Test drown and two option of items
		knights, items = knight_game.run_game('./moves.txt')
		r, b, g, y =  knights
		a,d,h,m = items
		self.assertEqual((r.name, r.position, r.item, r.status, r.attack, r.defence ), ('red', None, None, 'DROWN', 0, 0))
		self.assertEqual((g.name, g.position, g.item , g.status, g.attack, g.defence), ('green',(7,7) , None, 'LIVE', 1, 1))
		self.assertEqual((y.name, y.position, y.item, y.status , y.attack, y.defence), ('yellow',None, None, 'DROWN', 0 , 0))
		self.assertTrue((b.item.name, b.attack) in [('axe', 3), ('dagger', 2)]) 
		self.assertEqual((b.name, b.position, b.status ), ('blue', (0,5), 'LIVE'))
		
		self.assertEqual(a.name, 'axe')
		self.assertTrue(a.owner.name == 'blue' if a.owner else a.position == (0, 5))
		self.assertEqual(d.name, 'dagger')
		self.assertTrue(d.owner.name == 'blue' if d.owner else d.position == (0, 5))
		self.assertEqual((h.name, h.position), ('helmet',(5,5) ))
		self.assertEqual((m.name, m.position), ('magic_staff',(5,2) ))

	def test_run_game_moves2(self):
		# This will test fight and dead knight		
		knights, items = knight_game.run_game('./moves2.txt')
		r, b, g, y =  knights
		a,d,h,m = items
		self.assertEqual((r.name, r.position, r.item.name, r.status, r.attack, r.defence ), ('red', (1,5), 'axe', 'LIVE', 3, 1))
		self.assertEqual((g.name, g.position, g.item , g.status, g.attack, g.defence), ('green',(7,7) , None, 'LIVE', 1, 1))
		self.assertEqual((y.name, y.position, y.item, y.status , y.attack, y.defence), ('yellow',(0,5), None, 'DEAD', 0 , 0))
		
		self.assertEqual((a.name,a.owner.name, a.get_position()), ('axe', 'red', (1,5)))
		self.assertEqual((m.name, m.position), ('magic_staff',(5,2) ))
		self.assertEqual((h.name, h.position), ('helmet',(5,5)))
		self.assertEqual((d.name, d.position), ('dagger',(0,5)))


	
if __name__ == "__main__":
	unittest.main()
	
	

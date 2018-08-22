class Knight:
	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.status = 'LIVE'
		self.item = None
		self.defence = 1
		self.attack = 1

	def update_attack_power(self, number):
		self.attack += number
	
	def update_position(self, position):
		self.position = position
	
	def update_defence_power(self, number):
		self.defence += number
	
	def is_alive(self):
		if self.status != 'LIVE':
			return False
		else:
			return True

	def died(self):
		self.status = 'DEAD'
		self.defence = 0
		self.attack = 0
		self.item = None

	def equipped(self, item):
		self.item = item
		item.set_owner(self)
		self.attack += item.attack
		self.defence += item.defence	

	def drown(self):
		self.attack = 0
		self.defence = 0
		self.position = None			
		self.status = 'DROWN'
		self.item = None



class Item:
	def __init__(self, name, position, attack, defence):
		self.name = name 
		self.position = position
		self.owner = None
		self.attack = attack
		self.defence = defence

	def get_position(self):
		if self.owner:
			return self.owner.position
		else:
			return self.position

	def set_owner(self, owner):
		self.owner = owner
		self.position = None
		
	def release(self, position):
		self.position = position
		self.owner = None 


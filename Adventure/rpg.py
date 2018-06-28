#basic adventure game with python

#create a base class for all game items

Weapons_list = {'Rusty Sword': 5, 'Sharp Sword':10, 'Great Sword':15, 'Sword of the Morning': 20}
Weapons_cost = {'Rusty Sword': 10, 'Sharp Sword':20, 'Great Sword':30, 'Sword of the Morning': 40}
class Basemodel:
	base_hp = 100
	base_attack = 10
	base_mana = 20
	base_armor = 0
	base_mr = 0
	base_class = None
	current_weapon = 'Empty'
	current_weapon_damage = 0
	current_inventory = ['Healing potion']
	char_alive = True
	current_hp = 100

	def __init__(self, name):
		self.name = name

	def auto_attack(self):
		damage = self.base_attack + self.current_weapon_damage
		return damage
	def check_inventory(self):
		bool(self.current_inventory)
		if not self.current_inventory :
			return print('Empty inventory')
		else:
			for items in self.current_inventory:
				print(items)

	def take_damage(self, inc_dam):
		if self.char_alive:
			self.current_hp = self.current_hp - inc_dam
		return self.current_hp
	
	def return_current_hp(self):
		return self.current_hp


class Warrior(Basemodel):
	# this is the setup to change the presets from the base model.
	def __init__(self, name):
		super().__init__(name)
		self.base_hp = 200
		self.base_attack = 20
		self.base_mana = 5
		self.base_armor = 5
		self.base_mr = 0
		self.base_class = 'Warrior'
		self.current_weapon = 'Rusty Sword'
		self.current_weapon_damage = 5
		self.current_inventory = ['Healing potion']
		self.char_alive = True
		self.current_hp = 200

	def change_weapon(self, weapon,dam):
		if weapon in self.current_inventory:
			self.current_weapon = weapon
			self.current_weapon_damage = dam
		else:
			return print('You do not have one')

bob = Warrior('bob')

print(bob.current_hp)





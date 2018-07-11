# A module that does inventory in a few ways
#Requirements set up a gear list, set up slots, print out total stat increases

#List of gear
Gear = { 'Bronze Helm': ['Head',10],
         'Bronze Chest' : ['Chest',20],
         'Bronze Leggings' : ['Legs',15],
         'Leather Gloves' : ['Gloves',5],
         'Rusty Sword' : ['Weapon',10],
         'Bronze Boots': ['Boots',10],
         'Blue Cape' :['Cape',10],
         'Epic Sword': ['Weapon', 300]
}

class Inventory:
    def __init__(self):
        self.name = ''
        self.armor = 0
        self.damage = 5
        self.inventory = {'Head' : ['empty',1],
                          'Chest' : ['empty',2],
                          'Legs' : ['empty',3],
                          'Gloves' : ['empty',4],
                          'Weapon' : ['empty',5],
                          'Boots' : ['empty',6],
                          'Cape' : ['empty',7]
        }

    def equip_gear(self, gear):

        if gear in Gear:
            slot = Gear.get(gear)[0]
            values = Gear.get(gear)[1]
            print('Equiping',gear)
            self.inventory.update({slot : [gear,values]})
        else:
            print("No such gear")

    def get_armor(self):
        armor = 0
        for items in self.inventory:
            if items != 'Weapon':
                armor_value = self.inventory.get(items)[1]
                armor += armor_value
        return armor

    def get_damage(self):
        damage = self.damage + self.inventory.get('Weapon')[1]
        return damage

    def display_stats(self):
        armor = self.get_armor()
        damage = self.get_damage()

        print("Your armor class is:",armor)
        print("Your damage is:",damage)

inv = Inventory()
inv.display_stats()
inv.equip_gear("Bronze Helm")
inv.equip_gear("Epic Sword")
inv.display_stats()
#gearchange = input("What gear are you adding? ")
#arms = inv.get_armor()
#print(arms)

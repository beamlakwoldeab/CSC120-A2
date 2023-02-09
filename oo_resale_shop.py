from computer import *

class ResaleShop():
    inventory = list
    def __init__ (self):
        self.inventory=[]

    def buy(self, computer: Computer):
        self.inventory.append(computer)

        # buying a computer (add to inventory)
        
    def sell(self, computer: Computer):
        # selling a computer (remove from inventory)
        self.inventory=self.inventory.remove(computer)

    def printInventory(self, computer:Computer):     
        #  printing the inventory
        for computer in self.inventory:
            computer.printDetails() # make a print details function in computer class
        # print(self.inventory)

def main():
    c1=Computer('Macbook pro!!!!!!!', 'Intel', '5gb', '5gb','windows', 2003, 400)
    store=ResaleShop()
    store.buy(c1)
    store.printInventory(c1)
    # print(store)
    # print(c1.description)
    # c1.refurbish()
    # print(c1.price)
main()
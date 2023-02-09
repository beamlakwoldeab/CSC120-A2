class Computer:
    description:str
    processor_type:str
    hard_drive_capacity:int
    memory:str
    operating_system: str
    year_made: int
    price : int
    def __init__(self, description, processor_type, hard_drive_capacity, memory,operating_system,year_made, price):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price

    def updatePrice(self, newPrice):
        self.price=newPrice

        # updating the price of an item in the inventory
    def updateOs (self, newOs):
        self.operating_system=newOs
    
    def printDetails(self):
        print(self.description,self.processor_type, self.hard_drive_capacity,self.memory,self.operating_system,self.year_made, self.price)
        # print(self.processor_type)
        # print(self.hard_drive_capacity)
        # print(self.memory)
        # print(self.operating_system)
        # print(self.year_made)
        # print(self.price)

    def refurbish(self) -> None:
        # refurbishing a computer (update price based on age of machine, optionally update OS)
        if 0 < self.year_made < 2000:
            self.price=0
        elif 2000 <= self.year_made < 2012:
            self.price=250
        elif 2012<= self.year_made < 2018:
            self.price=550
        else:
            self.price=1000

        #this is not working
   
c1=Computer('Macbook pro!!!!!!!', 'Intel', '5gb', '5gb','windows', 2003,400)
c1.printDetails()

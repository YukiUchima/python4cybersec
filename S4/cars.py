class Car:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        self.gas = 0

    def get_gas(self):
        self.gas += 10

    def check_gas(self):
        print(self.gas)

    
def random_thing():
    print('Printing random thing!')
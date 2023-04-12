class Car:
    
    __odometer = 0 #km

    def __init__(self,make, model,year,color=None):
        self.make = make
        self.model = model
        self.year = year
        self.colour = color

    def Drive(self):
        print(self.model + " is driving ")

    def PrintInfo(self):
        print ("make : %s \n \ model : %s \n\ Year : %s \n\ colour :%s \n\ ", self.make, self.model,self.year,self.colour)


class Truck:
    make: None
    model: None
    year:None
    colour:None

    def Drive():
        print(" Truck is driving ")


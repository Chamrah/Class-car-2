# Define a class
class car():
    def __init__(self, speed, enginePower, color, name):
        self.speed = speed
        self.enginePower = enginePower
        self.color = color
        self.name = name

# Function that avoid repetition of the sentence
    def cars(self):
        print("the speed of this car {} ,enginePower {}, color {}, name{} ".format(self.speed, self.enginePower, self.color,self.name))

# Nominate the information of car
car1 = car("400KM", 400, "+Red","Mazda")

car1.cars()

        
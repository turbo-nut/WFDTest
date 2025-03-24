# part A programme for part B

# number = 4, vehicle
# attr= name, year, max_speed, mileage, color

class Vehicle:
    def __init__(self, name, year, max_speed, mileage, color):
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

        # print attr
    def printAttr(self):
        print(self.name)
        print(self.year)
        print(self.max_speed)
        print(self.mileage)
        print(self.color)

    def setName(self, name):
        if type(name) is str:
            self.name = name
        else:
            raise Exception("Name must be a string")

    def setYear(self, year):
        if type(year) is int:
            self.year = year
        else:
            raise Exception("Year must be an integer")

    def setMaxSpeed(self, max_speed):
        if type(max_speed) is int:
            self.max_speed = max_speed
        else:
            raise Exception("Speed must be an integer")

    def setMileage(self, mileage):
        if type(mileage) is int:
            self.mileage = mileage
        else:
            raise Exception("Mileage must be an integer")

    def setColor(self, color):
        if type(color) is str:
            self.color = color
        else:
            raise Exception("Color must be a string")


class Motorbike(Vehicle):
    def __init__(self, name, year, max_speed, mileage, color, owner, isInsured):
        super().__init__(name, year, max_speed, mileage, color)
        self.owner = owner
        self.isInsured = isInsured

    def setOwner(self, owner):
        if type(owner) is str:
            self.owner = owner
        else:
            raise Exception("Name of owner must be a string")

    def setInsurance(self, isInsured):
        if type(isInsured) is bool:
            self.isInsured = isInsured
        else:
            raise Exception("Insurance status can only be true or false")


if __name__ == "__main__":
    toyota = Vehicle('prius', 2004, 170, 50750, 'red')
    toyota.printAttr()
    toyota.setColor('red')
    toyota.setName('Carolla')
    print("")
    toyota.printAttr()
    print("")

    harley = Motorbike('Cruiser', 1995, 250, 10500, 'black', 'John Doe', True)
    harley.printAttr()
    harley.setColor('blue')
    harley.setInsurance(False)
    print("")
    harley.printAttr()

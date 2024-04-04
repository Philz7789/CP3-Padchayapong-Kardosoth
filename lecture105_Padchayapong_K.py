class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    def sayHz(self):
        print("I'm a red pickup")
class Car(Vehicle):
    def sayHa(self):
        print("I'm a blue car")
class Van(Vehicle):
    def sayHx(self):
        print("I'm a gray van")

pickup1 = Pickup
pickup1.turnOnAirConditioner(Vehicle)
pickup1.sayHz(self=Pickup)

car1 = Car
car1.turnOnAirConditioner(Vehicle)
car1.sayHa(self=Car)

van1 = Van
van1.turnOnAirConditioner(Vehicle)
van1.sayHx(self=Van)

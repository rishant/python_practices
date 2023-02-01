class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage =mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("Mileage of vehicle is ", self.mileage)
        print("Cost of vehicle is ", self.cost)
        print("I am a vehicle")

v1 = Vehicle(300,500)
v1.show_vehicle_details()

print("----------------------------------------------------------------")
# single level inheritance
class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        # call parent class constructor and pass parameter.
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ", self.tyres)
        print("Value of horse power is ", self.hp)

c2 = Car(500,800,4,300)
c2.show_vehicle_details()
c2.show_car_details()

print("----------------------------------------------------------------")
# multi level inheritance
class FlingCar(Car):

    def __init__(self,mileage,cost,tyres,hp,isFlyable):
        # call parent class constructor and pass parameter.
        super().__init__(mileage,cost,tyres,hp)
        self.isFlyable= isFlyable

    def show_car_details(self):
        print("I am a car")
        print("Number of tyres are ", self.tyres)
        print("Value of horse power is ", self.hp)
        print("Can car fly ", self.isFlyable)

c3 = FlingCar(500,800,4,300,True)
c3.show_vehicle_details()
c3.show_car_details()

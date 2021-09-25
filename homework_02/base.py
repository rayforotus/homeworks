from homework_02 import exceptions


class Vehicle:

    def __init__(self, weight = 100 , fuel = 50, fuel_consumption = 5, started = False):
       self.weight = weight
       self.fuel = fuel
       self.fuel_consumption = fuel_consumption
       self.started = started

    def start(self):
        if self.started != True:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        if  self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel()


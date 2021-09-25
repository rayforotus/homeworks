from homework_02 import base
from homework_02 import exceptions
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(base.Vehicle):
    cargo = 0
    max_cargo = 200

    def __init__(self,weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def load_cargo(self,add_cargo):
        if self.cargo + add_cargo <= self.max_cargo:
            self.cargo = self.cargo + add_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp

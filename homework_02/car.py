"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base
from engine import Engine
from homework_02 import engine


class Car(base.Vehicle):
    engine = None

    def set_engine(self,engine):
        self.engine = engine


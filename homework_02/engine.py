"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine():
    volume : int
    pistons : int


    # def __init__(self,volume = 5 ,pistons = 10):
    #     self.volume = volume
    #     self.pistons = pistons
    #

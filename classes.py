"""
Объекты расположены здесь
"""

from abc import ABC, abstractmethod


class Robot:
    code: str
    name: str
    _instances = {}

    def __new__(self, code: str, name:str)->None:
        self.code = code
        self.name = name
        if self not in self._instances:
            instance = super().__new__(self)
            self._instances[self] = instance
        return self._instances[self]


class Building(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.floors = 1


class House(Building):
    def __init__(self, floors:int = 1) -> None:
        super().__init__()
        self.floors = floors


class Barn(Building):
    def __init__(self) -> None:
        super().__init__()
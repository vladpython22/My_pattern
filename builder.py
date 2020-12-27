#Интерфейс для пошагового создания сложных объектов

from abc import ABC, abstractmethod


class InterfaceHouseBuilder(ABC):
    """The Builder Interface"""

    @abstractmethod
    def set_wall_material(value):
        """Set the wall_material"""

    @abstractmethod
    def set_building_type(value):
        """Set the building_type"""

    @abstractmethod
    def set_number_doors(value):
        """Set the number of doors"""

    @abstractmethod
    def set_number_windows(value):
        """Set the number of windows"""

    @abstractmethod
    def get_result(self):
        """Return the house"""


class HouseBuilder(InterfaceHouseBuilder):
    def __init__(self):
        self.house = House()

    def set_wall_material(self, value):
        self.house.wall_material = value
        return self

    def set_building_type(self, value):
        self.house.building_type = value
        return self

    def set_number_doors(self, value):
        self.house.doors = value
        return self

    def set_number_windows(self, value):
        self.house.windows = value
        return self

    def get_result(self):
        return self.house


class House():
    """The Product"""

    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_material="Brick"):
        #brick, wood, straw, ice
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hut, Castle, Duplex, HouseBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return "This is a {0} {1} with {2} door(s) and {3} window(s).".format(
            self.wall_material, self.building_type, self.doors, self.windows
        )


class IglooDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice")\
            .set_number_doors(1)\
            .set_number_windows(0)\
            .get_result()


class CastleDirector:
    """The Director, building a different representation."""
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("Castle")\
            .set_wall_material("Granite")\
            .set_number_doors(100)\
            .set_number_windows(200).get_result()


if __name__ == "__main__":
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    print(IGLOO)
    print(CASTLE)

from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def create_mersedes(self):
        pass

    def plan_creating(self):
        mersedes = self.create_mersedes()
        result = f"Factory: {mersedes.interface()}"
        return result


class Sedan(Creator):
    def create_mersedes(self):
        return SedanMersedes()


class Coupe(Creator):
    def create_mersedes(self):
        return CoupeMersedes()


class CarsInterface(ABC):
    def interface(self):
        pass


class SedanMersedes(CarsInterface):
    def interface(self):
        return f'Sedan of Mersedes'


class CoupeMersedes(CarsInterface):
    def interface(self):
        return f'Coupe of Mersedes'


def client_code(creator: Creator) -> None:
    print(f"Client: All is okay.\n"
          f"{creator.plan_creating()}", end="")


if __name__ == "__main__":
    print("SedanMersedes .")
    client_code(Sedan())
    print("\n")

    print("CoupeMersedes")
    client_code(Coupe())

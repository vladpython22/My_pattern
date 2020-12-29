class SingletonMeta(type):
    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            instance = super().__call__(*args, **kwargs)
            cls._inst[cls] = instance
        return cls._inst[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Mission complete")
    else:
        print("Faield")

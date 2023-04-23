class Engine:
    def __init__(self):
        self.__state = False
        self.__oil = False

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value: bool):
        self.__state = value

    @property
    def oil(self):
        return self.__oil

    @oil.setter
    def oil(self, oil: bool):
        self.__oil = oil
    def print(self):
        return "Двигатель заведен" if self.__state else "Двигатель не заведен"

    def oil_print(self):
        return "Масло в двигателе в пределах нормы" if self.__oil else "Масло не в пределах нормы"


class GasEngine(Engine):
    pass

class DieselEngine(Engine):
    pass


# Класс миксин Состояние двиагателя
class EngineCondition:
    @staticmethod
    def get_state(engine: Engine):
        print(engine.print())

# миксин наличие масла в двигателе
class EngineOil:
    @staticmethod
    def show_oil_engine(engine: Engine):
        print(engine.oil_print())





class Car(EngineCondition, EngineOil, TiresWheelsCondition):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color

    def __str__(self):
        return f"Марка: {self.__brand} год: {self.__year} цвет: {self.__color}"



def execute_application():

    engine = DieselEngine()
    car = Car("Mersedes", 2020, "black")
    car.get_state(engine)
    engine.state = True
    car.get_state(engine)

    car.show_oil_engine(engine)
    engine.oil = True
    car.show_oil_engine(engine)


if __name__ =="__main__":
    execute_application()
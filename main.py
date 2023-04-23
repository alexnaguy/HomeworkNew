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





def execute_application():



if __name__ =="__main__":
    execute_application()
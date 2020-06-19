class ConsultaPet():
    def __init__(self, pet, motivo_consulta, data=""):
        self.__pet = pet
        self.__data = data
        self.__motivo_consulta = motivo_consulta

    @property
    def pet(self):
        return self.__pet

    @pet.setter
    def pet(self, pet):
        self.__pet = pet

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def motivo_consulta(self):
        return self.__motivo_consulta

    @motivo_consulta.setter
    def motivo_consulta(self, motivo_consulta):
        self.__motivo_consulta = motivo_consulta
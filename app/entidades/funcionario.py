class Funcionario():
    def __init__(self, nome, nascimento, cargo, user):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cargo = cargo
        self.__user = user

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
class Pai:
    def __new__(cls):
        print("Método __new__ da classe Pai foi chamado")
        return super().__new__(cls)

class Filho(Pai):
    def __new__(cls):
        print("Método __new__ da classe Filho foi chamado")
        print(super())
        return super().__new__(cls)

# Criando uma instância da classe Filho
filho = Filho()

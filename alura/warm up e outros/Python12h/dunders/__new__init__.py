class Exemplo:
    def __new__(cls, *args, **kwargs):
        print("Método __new__ foi chamado")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, valor):
        print("Método __init__ foi chamado")
        self.valor = valor

# Criando uma instância da classe Exemplo
exemplo = Exemplo(10)
"""
"""
"""
Singleton é uma estratégia na criação de classes para permitir que somente uma instancia de objetos dessa classe possa ser
instanciada em toda da aplicação, note que se a instancia já existir a classe retorna instancia existente. Muito util para classes como
Banco de dados para criar apenas um objeto que se conecta ao banco.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Uso
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True

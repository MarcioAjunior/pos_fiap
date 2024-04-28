from collections import deque

class Fila:
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.fila = deque()
        return cls._instance
    
    def __init__(self) -> None:
        pass
    
    def addFila(self, elemento):
        self.fila.append(elemento)
        
    def removeFila(self):
        self.fila.popleft()
        
    def __repr__(self) -> str:
        return str(list(self.fila))


    
if __name__ == '__main__':
    fila = Fila()
    fila.addFila(10)
    print(fila)
    fila.addFila(20)
    print(fila)
    fila.removeFila()
    print(fila)
    fila2 = Fila()
    print('Fila 2',fila2)
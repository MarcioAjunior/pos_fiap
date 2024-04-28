class Pilha:
    _instance = None

    def __new__(cls) :
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.pilha = []
        return cls._instance
    
    def addPilha(self, elemento):
        self.pilha.append(elemento)
    
    def removePilha(self):
        self.pilha.pop()
        
    def __repr__(self) -> str:
        return ', '.join((str(x) for x in self.pilha))
    
if __name__ == '__main__':
    
    pilha = Pilha()
    pilha.addPilha(10)
    print(pilha)
    pilha.addPilha(20)
    print(pilha)
    pilha.removePilha()
    print(pilha)
    
    
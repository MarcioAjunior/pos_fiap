
class Retangulo:
    
    #Inicializador e não construtor !
    def __init__(self, lado_a : int, lado_b : int) -> None:
        self.lado_a = lado_a
        self.lado_b = lado_b
        
    def caucula_area(self):
        area = self.lado_a * self.lado_b
        return area
    
    def calcula_perimetro(self) -> int:
        perimetro = 2*self.lado_a + 2*self.lado_b
        return perimetro 
    
    def __repr__(self) -> str:
        return f'O retangulo possúi os lados {self.lado_a} e {self.lado_b} '
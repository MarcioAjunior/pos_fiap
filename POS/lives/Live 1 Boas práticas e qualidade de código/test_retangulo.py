from calculo_ret.live_01 import Retangulo

retangulo = Retangulo(10,15)

def test_lado():
    assert isinstance(retangulo.lado_a, int) 
    
def test_area():
    pass
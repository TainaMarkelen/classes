def main():
    t = Triangulo(10, 20, 30)
    
    triangulo = Triangulo(5, 10, 15)
    
    
    
    print (t.semelhantes(triangulo)) # a função main chamou o que deve ser colocado como parametro, no caso t, aí triangulo segue com um objeto da classe Triangulo

class Triangulo:
    # construtor da classe
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c:
            return 'isósceles'
        else:
            return 'escaleno'
        
    def retangulo(self):
        if self.a**2 == self.b**2 + self.c**2 or self.c**2 == self.a**2 + self.c**2 or self.c**2 == self.b**2 + self.a**2:
            return True
        else:
            return False
        

    def semelhantes(self, triangulo):
        t2 = triangulo
        if self.a / t2.a == self.b / t2.b == self.c / t2.c:
            return True
        else:
            return False
            

    
main()
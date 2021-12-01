''' Em alguns casos é necessário refatorar/reorganizar o código para que ele seja testável '''
''' O recomendável é ele retornar os valores ao invés de printar '''
# transformar em código orientado a objetos

import math
class Bhaskara:
    def delta(self, a, b, c):
        return (b ** 2) - 4 * a * c
    
    def main(self):
        a = float(input("Informe um número para a: "))
        b = float(input("Informe um número para b: "))
        c = float(input("Informe um número para c: "))
        print(self.calcula_raizes(self, a, b, c))
    
    # para testar basta chamar o calcula_raizes e testar com diversos valores
    def calcula_raizes(self,a, b, c):
        d = self.delta(a, b, c)
        if d == 0:
            raiz1 = ( -b + (math.sqrt(d))) // (2 * a)
            return 1, raiz1 # o número 1 é para indicar que tem uma única raíz
        else:
            if d < 0:
                return 0 # o 0 indica que não há raízes
            else:
                raiz1 = ( -b + (math.sqrt(d))) // (2 * a)
                raiz2 = ( -b - (math.sqrt(d))) // (2 * a)
                return 2, raiz1, raiz2 # o 2 é para indicar que tem duas raízes
      
'''b = Bhaskara()
   b.main()''' # para rodar o programa
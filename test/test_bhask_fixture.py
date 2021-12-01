''' É um valor fixo para um conjunto de testes '''
''' É usado muitas vezes para guardar um objeto que requer um pouco mais de trabalho para ser criado '''
''' Para definir uma fixture implementamos uma função que cria o objeto e a marcamos com @pytest.fixture, lembrando que é preciso importar o modulo antes'''

from exercicios_envolvendo_classes.src import bhask
import pytest
# cria-se uma classe de testes, começando com Test, para o python identificar
class TestBhaskara:
    
    @pytest.fixture
    def b(self):
        return bhask.Bhaskara() # Retorna a classe baskhara sempre que b for chamado
    
    def testa_uma_raiz(self, b):
        # passa como parametro e não precisa mais daquela linha anterior, em test_bhaskara
        assert b.calcula_raizes(1, 0, 0) == (1, 0) # o b devolve a classe bhaskara, que possui a função calcula_raizes
        
    def testa_duas_raizes(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
        
    def testa_zero_raizes(self, b):
        assert b.calcula_raizes(10, 10, 10) == (0)
        
    def testa_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
from exercicios_envolvendo_classes.src import bhask
# cria-se uma classe de testes, começando com Test, para o python identificar
class TestBhaskara:
    def testa_uma_raiz(self):
        # criando uma instancia da classe definiçoes
        b = bhask.Bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0)
        
    def testa_duas_raizes(self):
        # criando uma instancia da classe definiçoes
        b = bhask.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)
        
    def testa_zero_raizes(self):
        # criando uma instancia da classe definiçoes
        b = bhask.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == (0)
        
    def testa_raiz_negativa(self):
        # criando uma instancia da classe definiçoes
        b = bhask.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
        
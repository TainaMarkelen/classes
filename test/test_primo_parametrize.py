import pytest # deve ser importado sempre que for usar fixture ou parametrização
from exercicios_envolvendo_classes.src import primo # mudei para exercicios_incluindo_classes

class TestPrimos:
    @pytest.mark.parametrize('entrada, esperado', [
    (2, 'primo'),
    (7, 'primo'),
    (10, 'não primo'),
    (3, 'primo')
    ])
    def test_primo(self, entrada, esperado):
        p = primo.Calc_primo()
        assert p.eh_primo(entrada) == (esperado)
        
    
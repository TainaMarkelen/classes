from exercicios_envolvendo_classes.src import bhask
import pytest

class TestBhaskara:
    @pytest.mark.parametrize('r1, r2, r3, esperado', [(1, 0, 0,(1,0)),(1, -5, 6,(2, 3, 2)),(10, 10,10,(0)),(10, 20, 10,(1, -1))])
    def test_raiz(self, r1, r2, r3, esperado):
        b = bhask.Bhaskara()
        assert b.calcula_raizes(r1, r2, r3) == esperado
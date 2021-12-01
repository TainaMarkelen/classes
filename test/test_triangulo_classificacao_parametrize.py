from exercicios_envolvendo_classes.src import triangulo_classificacao
import pytest

class TestTrianguloRetangulo:
    @pytest.mark.parametrize('a, b, c, esperado' , [
    (1, 3, 5, False),
    (3, 4, 5, True)
    ])
    
    def test_classificacao(self, a, b, c, esperado):
        r = triangulo_classificacao.Triangulo(a, b, c)
        
        assert r.retangulo() == esperado
from exercicios_envolvendo_classes.src import triangulo_semelhante
import pytest

class TestTrianguloSemelhante:
    @pytest.mark.parametrize('a, b, c, a2, b2, c2, esperado', [(2, 2, 2, 4, 4, 4, True)])
    def test_semelhantes(self, a, b, c, a2, b2, c2, esperado):
        s = triangulo_semelhante.Triangulo(a, b, c)
        triangulo = triangulo_semelhante.Triangulo(a, b, c)
        triangulo.a = a2
        triangulo.b = b2
        triangulo.c = c2
        
        assert s.semelhantes(triangulo) == esperado
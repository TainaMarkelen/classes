from exercicios_envolvendo_classes.src import triangulo_tipo
import pytest

class TestTriangulo:
    @pytest.mark.parametrize('a, b, c, esperado', [
    (10, 10, 10, 'equilátero'),
    (10, 20, 10, 'isósceles'),
    (10, 20, 30, 'escaleno')
    ])
    
    def test_tipo(self, a, b, c, esperado):
        t = triangulo_tipo.Triangulo(a, b, c)
        
        assert t.tipo_lado() == esperado # não precisa colocar os parametros pois há o metodo __init__, que é o construto da classe
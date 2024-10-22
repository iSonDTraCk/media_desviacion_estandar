import unittest
from src.calculadora import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular


class TestCalculadora(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    def test_media_dos_elementos(self):
        self.assertEqual(calcular_media([4, 6]), 5)

    def test_media_elementos_positivos(self):
        self.assertEqual(calcular_media([10, 20, 30]), 20)

    def test_media_todos_ceros(self):
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_elementos_positivos_y_negativos(self):
        self.assertEqual(calcular_media([-10, 0, 10]), 0)

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_media([10, "20", 30])

    def test_desviacion_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)

    def test_desviacion_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([4, 6]), 1)

    def test_desviacion_elementos_positivos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([10, 20, 30]), 8.164965809)

    def test_desviacion_todos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0]), 0)

    def test_desviacion_elementos_positivos_y_negativos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([-10, 0, 10]), 8.164965809)

    def test_desviacion_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([10, "20", 30])


if __name__ == '__main__':
    unittest.main()

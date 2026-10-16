# test_ecuacion.py
import unittest
from ecuacion import resolver_ecuacion

class TestResolverEcuacion(unittest.TestCase):

    # 1. Caso base: Dos soluciones reales
    def test_dos_soluciones_reales(self):
        """x^2 - 5x + 6 = 0 => x=3, x=2"""
        res = resolver_ecuacion(1, -5, 6)
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertAlmostEqual(res["soluciones"][0], 3.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)

    # 2. Caso base: Una solución (raíz doble)
    def test_una_solucion(self):
        """x^2 - 2x + 1 = 0 => x=1"""
        res = resolver_ecuacion(1, -2, 1)
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertAlmostEqual(res["soluciones"], 1.0)

    # 3. Caso base: Sin solución real
    def test_sin_solucion_real(self):
        """x^2 + 1 = 0 => sin solucion real"""
        res = resolver_ecuacion(1, 0, 1)
        self.assertEqual(res["tipo"], "sin_solucion_real")
        self.assertEqual(res["soluciones"], [])

    # 4. Caso base: Ecuación lineal (a = 0)
    def test_ecuacion_lineal(self):
        """0x^2 + 2x + 4 = 0 => x = -2 (lineal)"""
        res = resolver_ecuacion(0, 2, 4)
        self.assertEqual(res["tipo"], "lineal")
        self.assertAlmostEqual(res["soluciones"][0], -2.0)

    # 5. Caso base: Coeficientes inválidos (a=0, b=0)
    def test_coeficientes_invalidos(self):
        """a=0, b=0 => ValueError"""
        with self.assertRaises(ValueError):
            resolver_ecuacion(0, 0, 5)

    # 6. Caso base: Múltiples casos con subTest
    def test_multiples_casos_con_subTest(self):
        """Varios casos parametrizados con subTest."""
        casos = [
            (1, 0, -4, "dos_soluciones", [2.0, -2.0]),
            (2, -4, 2, "una_solucion", 1.0),
            (1, 2, 5, "sin_solucion_real", []),
        ]
        for a, b, c, tipo_esp, sol_esp in casos:
            with self.subTest(a=a, b=b, c=c):
                res = resolver_ecuacion(a, b, c)
                self.assertEqual(res["tipo"], tipo_esp)
                if isinstance(sol_esp, list):
                    for obt, esp in zip(res["soluciones"], sol_esp):
                        self.assertAlmostEqual(obt, esp)
                else:
                    self.assertAlmostEqual(res["soluciones"], sol_esp)

    # --- RETO: 3 Pruebas Nuevas ---

    # 7. Reto 1: Coeficiente 'a' negativo
    def test_coeficiente_a_negativo(self):
        """-1x^2 + 0x + 4 = 0 => x1=-2.0, x2=2.0"""
        res = resolver_ecuacion(-1, 0, 4)
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertAlmostEqual(res["soluciones"][0], -2.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)

    # 8. Reto 2: Ecuación x^2 = 0 (solución cero)
    def test_solucion_cero(self):
        """1x^2 + 0x + 0 = 0 => x=0.0"""
        res = resolver_ecuacion(1, 0, 0)
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertAlmostEqual(res["soluciones"], 0.0)

    # 9. Reto 3: Todos los coeficientes cero
    def test_todos_coeficientes_cero(self):
        """a=0, b=0, c=0 => ValueError"""
        with self.assertRaises(ValueError):
            resolver_ecuacion(0, 0, 0)

if __name__ == '__main__':
    unittest.main()
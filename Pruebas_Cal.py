from Calculadora import Calculadora
import unittest

class Pruebas_Cal(unittest.TestCase):
	def setUp(self):
		self.calc = Calculadora()

	def test_suma_1(self):
        	self.assertEqual(self.calc.Suma(-456, -321), -777)
	def test_suma_2(self):
        	self.assertEqual(self.calc.Suma(98762, 34589), 133351)
	def test_suma(self):
        	self.assertEqual(self.calc.Suma(986858745342, 243547585689), 1230406331031)

	def test_resta_1(self):
		self.assertEqual(self.calc.Resta(-800, -200), -600)
	def test_resta_2(self):
                self.assertEqual(self.calc.Resta(56709, 18912), 37797)
	def test_resta_3(self):
                self.assertEqual(self.calc.Resta(185926346782, 287643629581), -101717282799)

	def test_producto_1(self):
                self.assertEqual(self.calc.Producto(-185, -957), 177045)
	def test_producto_2(self):
                self.assertEqual(self.calc.Producto(32569, 3), 97707)
	def test_producto_3(self):
                self.assertEqual(self.calc.Producto(515752648544, 8), 4126021188352)

	def test_division_1(self):
                self.assertEqual(self.calc.Division(-655, -25), 26.2)
	def test_division_2(self):
		self.assertEqual(self.calc.Division(25200, 24), 1050)
	def test_division_3(self):
		self.assertEqual(self.calc.Division(600400800246, 6), 100066800041)

	def test_potencia_2_1(self):
		self.assertEqual(self.calc.Potencia_2(-698), 487204)
	def test_potencia_2_2(self):
		self.assertEqual(self.calc.Potencia_2(65984), 4353888256)
	def test_potencia_2_3(self):
		self.assertEqual(self.calc.Potencia_2(85695896), 7343786591242816)

	def test_potencia_n_1(self):
		self.assertEqual(self.calc.Potencia_n(-325, 3), -34328125)
	def test_potencia_n_2(self):
		self.assertEqual(self.calc.Potencia_n(1234, 4), 2318785835536)
	def test_potencia_n_3(self):
		self.assertEqual(self.calc.Potencia_n(18262355, 2), 333513610146025)

	def test_raiz_cuadrada_1(self):
		with self.assertRaises(ValueError):
			self.calc.Raiz_cuadrada(-58)
	def test_raiz_cuadrada_2(self):
		self.assertEqual(self.calc.Raiz_cuadrada(23), 4.795831523312719)
	def test_raiz_cuadrada_3(self):
		self.assertEqual(self.calc.Raiz_cuadrada(5548997), 2355.630913364825)
if __name__ == '__main__':
	unittest.main()

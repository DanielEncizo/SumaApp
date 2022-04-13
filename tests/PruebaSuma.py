import unittest
from src.logica.Suma import Suma

class PruebaSuma(unittest.TestCase):
    def setUp(self):
        self.suma = Suma()

    def tearDown(self):
        self.suma=None

    def test_operacionSuma_dosNumerosPositivos_retornaSuma(self):
        # Arrange
        self.minuendo=10
        self.sustraendo=20
        self.resultadoesperado=30

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.minuendo, self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)

    def test_operacionSuma_dosNumerosNegativos_retornaSuma(self):
        # Arrange
        self.minuendo=-3
        self.sustraendo=-7
        self.resultadoesperado=-10

        # Do
        self.resultadoActual=self.suma.operacionSuma(self.minuendo, self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)

    def test_operacionSuma_dosNumerosPositivos_retornaResta(self):
        # Arrange
        self.minuendo=60
        self.sustraendo=20
        self.resultadoesperado=40

        # Do
        self.resultadoActual=self.suma.operacionResta(self.minuendo, self.sustraendo)

        # Assert
        self.assertEqual(self.resultadoesperado,self.resultadoActual)
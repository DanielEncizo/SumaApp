import unittest
from src.logica.Operaciones import Operaciones

class SumaTests ( unittest.TestCase ) :
    def test_suma_dosNumeros_retornaSuma ( self ) :
        # arrange
        op=Operaciones()
        sumando1=5
        sumando2=3
        resultadoEsperado=8

        # do
        resultadoActual=op.suma(sumando1,sumando2)
        # Assert
        self.assertEqual ( resultadoEsperado , resultadoActual )



# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
from CreditCard.Payments import CreditCardCalculator, ExcesiveInterestException

# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):
    """
    Unit Tests for monthly payment calculation

    Pruebas unitarias para el pago mensual de las compras con tarjeta de credito
    """

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        amount = 200000
        interest = 3.1
        periods = 36
        payment = 9297.96
        result = CreditCardCalculator.calcPayment( amount, interest, periods )
        # Prueba que dos variables sean iguales
        self.assertEqual( payment, round(result,2)  )

    def testPayment1_1(self):
        amount = 850000
        interest = 3.4
        periods = 24
        payment = 52377.5
        result = CreditCardCalculator.calcPayment( amount, interest, periods )
        self.assertEqual( payment, round(result,2)  )

    def testPayment2(self):
        """ amount normal con todos los parametros correctos """
        amount = 480000
        interest = 0
        periods = 48
        payment = 10000

        result = CreditCardCalculator.calcPayment( amount, interest, periods )

        self.assertEqual( payment, round(result,2)  )


    def testPayment4(self):
        """  amount a una sola payment """
        amount = 90000
        interest = 2.4
        periods = 1
        payment = 90000
        result = CreditCardCalculator.calcPayment( amount, interest, periods )
        self.assertEqual( payment, round(result,2)  )

    def testPayment3(self):
        """ amount con interest excesiva """
        amount = 50000
        interest = 12.4
        periods = 60
        
        try:
            result = CreditCardCalculator.calcPayment( amount, interest, periods )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( result, 0 )  # Forzar fallo caso
        except  ExcesiveInterestException :
            pass  # Forzar Exito

    def testPayment3_v2(self):
        """ amount con interest excesiva """
        amount = 50000
        interest = 12.4
        periods = 60
        # Para controlar que una funcion si genere una excepcion
        # en el caso de prueba, se usa el metodo assertRaises
        # el primer parametro es la Excepcion esperada
        # el segundo es el metodo que se va a invocar
        # y los demas parametros son los parametros del metodo bajo prueba
        self.assertRaises( ExcesiveInterestException,  CreditCardCalculator.calcPayment, amount, interest, periods )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcPayment.__doc__)
    unittest.main()
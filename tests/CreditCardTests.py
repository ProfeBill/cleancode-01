import sys
sys.path.append("src")

# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
from model.Payments import CreditCardCalculator, ExcesiveInterestException, Purchase

# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):
    """
    Unit Tests for monthly payment calculation

    Pruebas unitarias para el pago mensual de las compras con tarjeta de credito
    """

    # Cada prueba unitaria es un metodo la clase
    def test_normal_1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        test_purchase = Purchase( amount = 200000, interest = 3.1, number_of_payments= 36)
        payment = 9297.96
        result = CreditCardCalculator.calculate_payment( test_purchase )
        # Prueba que dos variables sean iguales
        self.assertEqual( payment, round(result,2)  )

    def test_normal_3(self):
        test_purchase = Purchase( amount = 850000, interest = 3.4, number_of_payments= 24)
        payment = 52377.5
        result = CreditCardCalculator.calculate_payment( test_purchase )
        self.assertEqual( payment, round(result,2)  )

    def test_normal_2(self):
        """ compra normal con todos los parametros correctos """
        test_purchase = Purchase(amount = 480000, interest = 0, number_of_payments= 48)
        payment = 10000

        result = CreditCardCalculator.calculate_payment( test_purchase )

        self.assertEqual( payment, round(result,2)  )


    def test_extra_4(self):
        """  compra a una sola payment """
        test_purchase = Purchase( amount = 90000, interest= 2.4, number_of_payments= 1)
        payment = 90000
        result = CreditCardCalculator.calculate_payment( Purchase )
        self.assertEqual( payment, round(result,2)  )

    def test_error_3(self):
        """ amount con interest excesiva """
        test_purchase = Purchase( amount=500000, interest=12.4, number_of_payments=60  )
        
        try:
            result = CreditCardCalculator.calculate_payment( test_purchase )
            # si no generó excepcion, quedo mal hecho el codigo
            self.assertEqual( result, 0 )  # Forzar fallo caso
        except  ExcesiveInterestException :
            pass  # Forzar Exito

    def test_error_3_v2(self):
        """ amount con interest excesiva """
        test_purchase = Purchase( amount = 50000,   interest = 12.4, number_of_payments= 60)
        # Para controlar que una funcion si genere una excepcion
        # en el caso de prueba, se usa el metodo assertRaises
        # el primer parametro es la Excepcion esperada
        # el segundo es el metodo que se va a invocar
        # y los demas parametros son los parametros del metodo bajo prueba
        self.assertRaises( ExcesiveInterestException,  CreditCardCalculator.calculate_payment, test_purchase )

# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcPayment.__doc__)
    unittest.main()
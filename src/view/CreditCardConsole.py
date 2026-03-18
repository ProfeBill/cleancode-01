"""

Interfaz de Usuario tipo consola para la funcionalidad de calcular la cuota de tarjeta de credito

"""
import sys
sys.path.append("src")
from model.Payments import CreditCardCalculator, Purchase

#  Obtener los datos de entrada
purchase_amount = float( input( "Ingrese el valor la compra: ") )
num_payments = int( input( "Ingrese el numero de cuotas: ") )
interest_rate = float( input( "Ingrese la tasa de interés: ") ) / 100

purchase = Purchase( amount=purchase_amount, interest=interest_rate, number_of_payments=num_payments  )


try:
    #  Realizar el proceso
    payment = CreditCardCalculator.calculate_payment( purchase )

    # Mostrar los datos de salida
    print( f"El valor de la cuota es: {payment}" )
except Exception as err :
    # Capturamos la excepcion, de una clase en particular y la guardamos en una variable
    print(f"Tia, no puedo calcular la cuota { err } "  )
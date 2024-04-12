# Maximun intrest rate allowed
MAX_INTEREST = 100/12

class ExcesiveInterestException( Exception ): 
    """ 
    Custom exception for interest rates above maximun

    Exepcion personalizada para indicar que una tasa de interes supera
    el tope máximo

    """
    def __init__( self, interest ):
        """
        To raise this exception, pass the intrest rate used as parameter to constructor

        Para usar esta excepción, debe llamar al constructor indicando la tasa usada
        """
        super().__init__( f"Invalid interest rate {interest} maximun allowed is {MAX_INTEREST}" )


class InvalidPurchaseException( Exception ): 
    """ 
    Exepcion personalizada para indicar que el valor de la compra es menor o igual a cero

    """
    def __init__( self ):
        super().__init__( f"Purchase amount must be greater than zero" )

class InvalidumberOfPaymentsException( Exception ): 
    """ 
    Exepcion personalizada para indicar que el nmero de cuotas es menor o igual a cero

    """
    def __init__( self ):
        super().__init__( f"Number of payments must be greater than zero" )


class CreditCardCalculator:
    """
    Class for financial operations for a Credit Card

    Clase para realizar operaciones financieras para una tarjeta de crédito
    """

    def calcPayment(amount : float,interest : float, number_of_payments : int):
        """
        Calculates the monthly payment for a purchase amount with a interest rate
        in a number of periods

        Calcula la cuota a pagar por una compra con una tarjeta de crédito

        Parameters
        ----------

        amount : float
            Purchase amount / Valor de la compra
        interest : float
            Monthly interest rate for purchase. Must be zero or positive less than
            MAX_INTEREST_RATE / Tasa maxima de interes, valor positivo menor que MAX_INTEREST_RATE          
        periods : int
            Number of monthly payments / Numero de cuotas a diferir la compra

        Returns
        -------
        payment : float
            Monthly payment calculated. Not rounded / Pago mensual calculado. El resultado no esta redondeado
        
        Raises
        ------
        ExcesiveInterestException
            When interest rate is above the valu defined in  MAX_INTEREST_RATE

        
        """
        
        # Para efectos de calcular el rendimiento se guarda la hora actual en esta variable
        execution_time = 0

        CreditCardCalculator.checkInterest(interest)

        CreditCardCalculator.CheckPayments(number_of_payments)

        CreditCardCalculator.CheckAmount(amount)

        if number_of_payments == 1 :
            """ 
            If periods equals one, no interests are calculated

            Cuando el plazo sea una sola cuota, no se aplican intereses 
            """
            return amount

        """ La tasa de interés está expresada como un entero entre 1 y 100 """
        i =  interest / 100
    
        if interest == 0:
            """ 
            Cuando la tasa sea cero, la cuota es la compra dividida las cuotas
            para evitar error de division por cero 
            """
            return amount / number_of_payments  # Divide el monto por la cantidad de cuotas
                                     # Retorna el interes a pagar
        else:         
            return (amount * i) / (1 - (1 + i) ** (-number_of_payments))

    def CheckAmount(amount):
        if amount <= 0 :
            raise InvalidPurchaseException()

    def CheckPayments(periods):
        if periods <= 0 :
            raise InvalidumberOfPaymentsException()

    def checkInterest(interest):
        """ 
        Verifica que la tasa de interés no supere la maxima permitida
        """
        if interest > MAX_INTEREST :
            """ 
            If interest rate is above MAX_INTEREST_RATE raises ExcesiveInterestException
            Si la tasa es mayor que MAX_INTEREST_RATE, arroja una excepcion ExcesiveInterestException """
            raise ExcesiveInterestException( interest )


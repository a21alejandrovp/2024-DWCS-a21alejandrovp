# TASK 3.6 - CALCULATOR CLASS
# ---------------------------
class Calculator:
    numberOfObjects = 0

    def __init__(self, num1=None, num2=None):
        self.num1 = num1
        self.num2 = num2
        Calculator.numberOfObjects += 1
        
        if self.num1 is not None and type(num1) != int and self.num2 is not None and type(num2) != int:
            raise Exception("The parameters are wrong!")

    def __str__(self):
        return(f'"CALCULE {Calculator.numberOfObjects}" --- "First number": {self.num1} --- "Second number": {self.num2}')

    def suma(self):
        return(f'La suma de {self.num1} y {self.num2} da como resultado {self.num1 + self.num2}')

firstCalcule = Calculator()
firstCalcule.num1 = 5
firstCalcule.num2 = 6
print(f'"CALCULE {Calculator.numberOfObjects}" --- "First number": {firstCalcule.num1} -- "Second number: ": {firstCalcule.num2}')

secondCalcule = Calculator(3, 4)
print(secondCalcule)
print(f'Función suma() de "CALCULE 2" - {secondCalcule.suma()}')
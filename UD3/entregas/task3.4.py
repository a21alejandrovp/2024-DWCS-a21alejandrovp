# TASK 3.4 - WRITE A FUNCTION TO CALCULATE THE FACTORIAL OF A NUMBER
# ------------------------------------------------------------------
def factorial(num): 
    if type(num) != int:
        raise Exception("The parameter must be an integer!")
    else:
        if num >= 0:
            contador = 1
            for num in range (1, num + 1): 
                contador *= num 
            return contador
        else:
            raise Exception("The parameter must be greater than 0!")
try: 
    print(factorial(5))
    print(factorial(-1))
except Exception as error:
    print(error)
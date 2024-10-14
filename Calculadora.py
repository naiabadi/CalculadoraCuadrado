#######################################################################################################################
#######################################################################################################################
# ENUNCIADO:
# Calculadora que solicite al usuario dos números y permita hacer las siguientes operaciones:
# Suma ; Resta ; Multiplicación ; División (*)
# * El 2º valor será distinto de cero. Para ello, introducir condición.
#######################################################################################################################
#######################################################################################################################
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print('ERROR DE OPERACION')

if __name__ == "__main__":

    a = int(input("Introduce el primer valor "))
    b = int(input("introduce el segundo valor "))
    c = input("introduce operacion ")

    if c.lower() == 'suma':
        print(suma(a, b))
    elif c.lower() == 'resta':
        print(resta(a, b))
    elif c.lower() == 'multiplicacion':
        print(multiplicacion(a, b))
    elif c.lower() == 'division':
        print(division(a, b))
    else:
        print('Vuelva a intentarlo con suma, resta, multiplicaion o division')

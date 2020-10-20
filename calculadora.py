#!usr/bin/python3

"""
Programa que ejecuta las operaciones básicas de
una calculadora
"""


def add(x, y):
    """
    función que ejecuta la suma de dos flotantes
        x: type(int)
        y: type(int)
    retorno x + y
    """
    try:
        return x + y
    except TypeError:
        print("Ingresa un entero")


def resta(x, y):
    """
    función que ejecuta la resta de dos flotantes
        x: type(int)
        y: type(int)
    retorno x - y
    """
    try:
        return x - y
    except TypeError:
        print("Ingresa un entero")


def multiply(x, y):
    """
    función que ejecuta la multiplicacion de dos flotantes
        x: type(int)
        y: type(int)
    retorno x * y
    """
    try:
        return x * y
    except TypeError:
        print("Ingresa un entero")
    except ValueError:
        print("Ingresa un entero")


def divide(x, y):
    """
    función que ejecuta la división de dos flotantes
        x: type(int)
        y: type(int)
    retorno x / y
    """
    try:
        return x / y
    except TypeError:
        print("Ingresa un entero")
    except ZeroDivisionError:
        print("No puedes dividir entre cero")


print("Seleccione una operación")
print("1. sumar")
print("2. restar")
print("3. Multiplicar")
print("4. Dividir")
print("Para salir del programa ejecuta Ctrl + C")


while True:
    # Take input from the user
    choice = input("Ingresa una opción(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = int(input("Ingresa el primer número: "))
            num2 = int(input("Ingresa el segundo número: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", resta(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
        except TypeError:
            print("Ingresa un número entero")
        except ValueError:
            print("Ingresa un número entero")
    else:
        print("entrada inválida")

# importo doctest como modulo principal
if __name__ == "__main__":
    import doctest
    doctest.testmod()

#libreria

import math
import random


def show_menu():
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz")
    print("7. senocoseno")
    print("8. valorAbsoluto")
    print("9. constanteEuler")
    print("10. aleatoreo")
    print("11. Salir")

def suma(a, b):
     return a + b
  
def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a,b):
    return math.sqrt(a)

def senocoseno(a,b):
    a = math.pi / a  # Convertir 45 grados a radianes
    c = math.sin(a)
    d = math.cos(a)
    print(f"El seno del angulo en radianes es: {c}, y el coseno es {d}")

def valorAbsoluto(a,b):
    valor_absoluto = math.fabs(a)
    print(f"el valor absoluto es: {valor_absoluto}")

def  Euler(a,b):
    euler_elevado = math.exp(a)
    print(f"la constante de euler en este caso es : {euler_elevado}")

def numAlet(a,b):
     numero_aleatorio = random.randint(a,b)
     print(f"El número aleatorio generado es:  {numero_aleatorio}")


# Diccionario de opciones
options = {
    "1": suma,
    "2": resta,
    "3": multiplicacion,
    "4": division,
    "5": potencia,
    "6": raiz,
    "7": senocoseno,
    "8": valorAbsoluto,
    "9": Euler,
    "10": numAlet,
    "11": exit,
}



# Ciclo principal del programa
while True:
    show_menu()
    choice = input("Ingresa el número de opción: ")

    # Ejecutar función correspondiente a la opción seleccionada
    if choice in options:
        if choice != "11":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            result = options[choice](num1, num2)
          
            print("El resultado es:", result)
            print("--------------------------------------")
        else:
            print("Saliendo del programa...")
            break
    else:
        print("Opción inválida, intenta de nuevo.")
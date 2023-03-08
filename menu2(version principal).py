import math
import random
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def raiz(a,b):
    return math.sqrt(a)

def potencia(a, b):
    return a ** b
    
def sencos(a,b):
    a = math.pi / a  # Convertir 45 grados a radianes
    c = math.sin(a)
    d = math.cos(a)
    print(f"El seno del angulo en radianes es: {c}, y el coseno es {d}")

def adbsoluto(a,b):
    valor_absoluto = math.fabs(a)
    print(f"el valor absoluto es: {valor_absoluto}")

def euler(a,b):
    euler_elevado = math.exp(a)
    print(f"la constante de euler en este caso es : {euler_elevado}")
def numAlet(a,b):
     numero_aleatorio = random.randint(a,b)
     print(f"El número aleatorio generado es:  {numero_aleatorio}")
def Basesnumericas(d):
    #conv. decimal binario
    binario = bin(d)
    print(f"binario: {binario}")
    #conv. decimal hexa
    hexa = hex(d)
    print(f"hexadecimal: {hexa}")
    #conv. decimal-octal
    octal = oct(d)
    print(f"octal: {octal}")



# Definimos la función para mostrar el menú y obtener la opción del usuario
def menu():
    print("=== CALCULADORA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. raiz")
    print("6. Potencia")
    print("7. Seno y coseno de un angulo en radianes")
    print("8. obtener el valor absoluto")
    print("9. Constante de euler")
    print("10. Generar numero aleatorio")
    print("11. decimal a bases numericas")
    print("11. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

# Definimos la función para obtener los operandos de las operaciones
def obtener_operandos():
    a = float(input("Ingrese el primer operando: "))
    b = float(input("Ingrese el segundo operando: "))
    return a, b

# Ejecutamos el programa
while True:
    opcion = menu()

    if opcion == 1:
        a, b = obtener_operandos()
        print("El resultado de la suma es:", suma(a, b))
    elif opcion == 2:
        a, b = obtener_operandos()
        print("El resultado de la resta es:", resta(a, b))
    elif opcion == 3:
        a, b = obtener_operandos()
        print("El resultado de la multiplicación es:", multiplicacion(a, b))
    elif opcion == 4:
        a, b = obtener_operandos()
        if b == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print("El resultado de la división es:", division(a, b))
    elif opcion == 5:
        print("el resultado sera del primer valor que ingreses :)")
        a, b = obtener_operandos()
        print("El resultado de la raiz es:", raiz(a,b))
    elif opcion == 6:
        a, b = obtener_operandos()
        print("El de la potencia es : ", potencia(a,b))
    elif opcion == 7:
        print("el resultado sera del primer valor que ingreses :)")
        a, b = obtener_operandos()
        print( sencos(a,b))
    elif opcion == 8:
        print("el resultado sera del primer valor que ingreses :)")
        a, b = obtener_operandos()
        print( adbsoluto(a,b))
        
    elif opcion == 9:
        print("el resultado sera del primer valor que ingreses :)")
        a, b = obtener_operandos()
        print( euler(a,b))
    elif opcion == 10:
        print("El primer valor sera el limite inferio y el segundo el limite superior :)")
        a, b = obtener_operandos()
        print( numAlet(a,b))
    elif opcion == 11:
        print("el resultado sera del primer valor que ingreses :)")
        d = int(input("digite el numero a transformar: "))
        print( Basesnumericas(d))
    
    elif opcion == 11:
        print("Adiós!")
        break
    else:
        print("Opción inválida. Por favor elija una opción válida.")

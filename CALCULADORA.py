
#libreria

import math
import random

#addiquirir informacion
a = int (input("digite el numero 1:"))
print(f"el numero a es:{a}")
b = int (input("digite el numero 2:"))
print(f"el numero a es:{b}")

#proceso
c = a + b
d = a - b
e = a * b
f = a / b
g = a ** b
h = math.sqrt(a)


#salida
print(f"el resultado de la suma es : {c}")
print(f"el resultado de la resta es : {d}")
print(f"el resultado de la multiplicación es : {e}")
print(f"el resultado de la división es : {f}")
print(f"el resultado de la potencia es : {g}")
print(f"el resultado de la raiz de a es : {h}")

#calcular el seno y coseno en radianes
cos = int (input("Cálculo del seno y coseno de un ángulo en radianes"))

angulo = math.pi / cos  # Convertir 45 grados a radianes
seno = math.sin(angulo)
coseno = math.cos(angulo)
print(f"El seno del angulo en radianes es: {seno}, y el coseno es {coseno}")

#calcular valor absoluto
ads = int (input("Función math para calcular un valor absoluto"))
x = ads
valor_absoluto = math.fabs(x)
print(f"el valor absoluto es: {valor_absoluto}")

#constante de euler
potencia = int (input("Función de la constante de euler"))
pot = potencia
euler_elevado = math.exp(potencia)

print(f"la constante de euler en este caso es : {euler_elevado}")
#generar un numero aleatoreo
print("Genere un numero aleatorio a su gusto: ")
limite_inferior = int(input("Ingrese el límite inferior: "))
limite_superior = int(input("Ingrese el límite superior: "))

numero_aleatorio = random.randint(limite_inferior, limite_superior)

print("El número aleatorio generado es:", numero_aleatorio)

#CALCULADORA SISTEMAS NUMERICOS
numero = int(input("digite el numero a transformar: "))
#conv. decimal binario
binario = bin(numero)
print(f"binario: {binario}")
#conv. decimal hexa
hexa = hex(numero)
print(f"hexadecimal: {hexa}")
#conv. decimal-octal
octal = oct(numero)
print(f"octal: {octal}")
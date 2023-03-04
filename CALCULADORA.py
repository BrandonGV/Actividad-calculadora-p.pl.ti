
#libreria

import math

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

cos = int (input("Cálculo del seno y coseno de un ángulo en radianes"))

angulo = math.pi / cos  # Convertir 45 grados a radianes
seno = math.sin(angulo)
coseno = math.cos(angulo)

print({seno}, coseno)  # Salida: 0.7071067811865475 0.7071067811865476"


rend = int (input("Cálculo del seno y coseno de un ángulo en radianes"))
x = rend
redondeado = round(x, 3)

print(redondeado)  # Salida: 3.142

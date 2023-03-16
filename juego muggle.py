from random import randint

secret_number = randint (1,10)

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

salir = False 

while salir == False :
    numero = int(input("Escribe el número correcto para salir: "))
    
    if numero != secret_number :
        print("¡Ja, ja! ¡Estás atrapado en mi bucle")
    else :
        print("Bien hecho, muggle! Eres libre ahora")
        salir = True
print("Fin del Juego")

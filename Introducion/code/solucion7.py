nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
anio_actual = 2023
anio_cumple_100 = anio_actual + (100 - edad)
print("Hola", nombre, ", cumplirás 100 años en el año", anio_cumple_100)

"""
En este código, se utiliza la función input() para solicitar al usuario que
ingrese su nombre, el cual es almacenado en la variable nombre. Luego, se
utiliza la función input() para solicitar al usuario que ingrese su edad, la
cual es almacenada en la variable edad. Posteriormente, se calcula el año en
el que el usuario cumplirá 100 años y se almacena en la variable
anio_cumple_100. Finalmente, se muestra por pantalla el nombre del usuario,
junto con el año en el que cumplirá 100 años.

1. La variable nombre almacena el nombre del usuario que ingresa mediante la 
   función input().
2. La variable edad almacena la edad del usuario que ingresa mediante la función 
   input(). La función int() se usa para convertir la entrada en un número entero.
3. La variable anio_actual almacena el año actual.
4. La variable anio_cumple_100 calcula el año en que el usuario cumplirá 100 años.
5. La función print() se utiliza para mostrar un mensaje al usuario, que incluye 
   su nombre, el año en que cumplirá 100 años.
"""
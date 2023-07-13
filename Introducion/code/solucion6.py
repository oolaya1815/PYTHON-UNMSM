numero = float(input("Ingrese un número flotante: "))

parte_entera = int(numero)
parte_decimal = round(numero - parte_entera,2)   #  3.45678 --> round(3.45678, 3) --> 3.457

print("La parte entera del número ingresado es:", parte_entera)
print("La parte decimal del número ingresado es:", parte_decimal)

"""
En este código, se utiliza la función input() para solicitar al usuario que
ingrese un número flotante, el cual es almacenado en la variable numero. Luego,
se obtiene la parte entera y decimal del número ingresado, las cuales son
almacenadas en las variables parte_entera y parte_decimal, respectivamente.
Finalmente, se muestra por pantalla la parte entera y decimal del número
ingresado.
"""
"""
crear un programa que ingrese por teclado 
una cantidad manzanas vendidas y de igual 
forma su precio
"""

cantidad = int(input("Ingrese la cantidad de manzanas vendidas: "))
precio = float(input("Ingrese el precio de las manzanas: S/. "))
total = cantidad * precio

print("El total a pagar es: S/.", total)
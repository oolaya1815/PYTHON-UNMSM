""" 
Calcular el indice de masa corporal de una persona
    - peso (Kg)
    - altura (m)
    Formula: peso / altura**2

peso = 67Kg
altura = 1.5m
imc = 67 / (1.5**2)
"""

peso = int(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = round(peso / (altura**2),2)

print("*"*55)
print("Su indice de masa corporal es: ", imc)
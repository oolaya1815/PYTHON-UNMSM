"""
Escribir un programa que permita calcular la ganacia
en una inversión de interes simple

    - capital
    - interes (%) --> 1.25%, 2.34%, 12.34%
    - tiempo (años)
    Formula: ganacias = capital * interes * tiempo
"""
capital = float(input("Ingrese el capital: S./ "))
interes = float(input("Ingrese el interes (%): "))
tiempo = int(input("Ingrese el tiempo (años): "))

ganancia = round(capital * (interes/100) * tiempo,2)

print("+"*54)
print("La ganancia es: S./", ganancia)
print("El monto a depositar es: S./", capital + ganancia)
numero = int(input("Ingrese un número entero: "))
paridad = ["par", "impar"]
print("El número es", paridad[numero % 2])

"""
Aquí, utilizamos la operación módulo % para 
determinar si el número es par o impar, y luego 
lo indexamos con una lista paridad que contiene 
las palabras "impar" y "par". El resultado es que 
se imprimirá la palabra correcta según corresponda.
"""
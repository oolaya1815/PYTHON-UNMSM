texto = input("Ingrese una cadena de texto: ")
caracteres = list(texto)
print(*caracteres, sep='\n')

"""
En este código, la función list(texto) convierte 
la cadena de texto ingresada por el usuario en una 
lista de caracteres. Luego, la función print(*caracteres, sep='\n')
 muestra cada elemento de la lista en una línea separada, 
 utilizando el operador de desempaquetado * para indicar 
 que queremos pasar cada elemento de la lista como un 
 argumento separado a la función print(), y el 
 argumento sep='\n' para indicar que queremos separar 
 cada elemento con un salto de línea.
"""
"""
Tenemos una tienda que se dedica a la venta de camisas
necesitamos crear un programa que calcule el total a pagar
por el cliente, ademas estamos brindando un descuento
tanto la cantidad, precio y descuento debe ser ingresado por
teclado

# - cantidad
# - precio
# - descuento

% => 1/100

cantidad = 100
precio = 200
descuento = 30

subtotal = cantidad * precio
des = subtotal * (descuento/100)
total = subtotal - des
"""
cantidad = int(input("Ingrese la cantidad de camisas: "))
precio = float(input("Ingrese el precio de las camisas: S./ "))
descuento = int(input("Ingrese el (%) descuento: "))

subtotal = cantidad * precio
descuento = subtotal * (descuento/100)
total = subtotal - descuento

print("El subtotal es: S/.", subtotal)
print("El descuento es: S/.", descuento)
print("El total a pagar es: S/.", total)
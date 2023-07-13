"""
Tenemos un emprendimiento, el cual envia a domicilio frutas
calcula el total a pagar por el cliente

 - cantidad
 - precio
 - precio de envio

"""
 
cantidad = int(input("Ingrese la cantidad de frutas: "))
precio = float(input("Ingrese el precio de las frutas: S./ "))
precio_envio = float(input("Ingrese el precio de envio: S./ "))

subtotal = cantidad * precio
total = subtotal + precio_envio

print("="*55)
print("El subtotal es: S./", subtotal)
print("El precio de envio es: S/.", precio_envio)
print("El total a pagar es: S/:", total)
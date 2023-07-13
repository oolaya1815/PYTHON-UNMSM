# Ejercicios

 1. Crea una clase llamada "Rectángulo" que tenga atributos de ancho y alto. Implementa métodos para calcular el área y el perímetro del rectángulo.

    ```python
    class Rectangulo:
        def __init__(self, ancho, alto):
            self.ancho = ancho
            self.alto = alto
        
        def calcular_area(self):
            return self.ancho * self.alto
        
        def calcular_perimetro(self):
            return 2 * (self.ancho + self.alto)
    
    rectangulo = Rectangulo(5, 3)
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())
    ```

 2. Crea una clase llamada "Estudiante" que tenga atributos de nombre y edad. Implementa un método para imprimir los datos del estudiante.

    ```python
    class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    estudiante = Estudiante("Juan", 20)
    estudiante.imprimir_datos()
    ```
    
 3. Crea una clase llamada "CuentaBancaria" que tenga atributos de número de cuenta y saldo. Implementa métodos para depositar dinero, retirar dinero y consultar el saldo.

    ```python
    class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo=0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def depositar(self, monto):
        self.saldo += monto
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")
    
    def consultar_saldo(self):
        return self.saldo

    cuenta = CuentaBancaria("12345")
    cuenta.depositar(1000)
    cuenta.retirar(500)
    print("Saldo:", cuenta.consultar_saldo())
    ```
    
 4. Crea una clase llamada "Tienda" que tenga atributos de nombre y lista de productos. Implementa métodos para agregar productos a la tienda, eliminar productos y mostrar la lista de productos.

    ```python
    class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
        else:
            print("El producto no existe")
    
    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    tienda = Tienda("Mi Tienda")
    tienda.agregar_producto("Camiseta")
    tienda.agregar_producto("Pantalón")
    tienda.eliminar_producto("Pantalón")
    tienda.mostrar_productos()
    ```
    
 5. Crea una clase llamada "Vehículo" que tenga atributos de marca, modelo y año. Implementa métodos para acelerar, frenar y mostrar información del vehículo.

    ```python
    class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def acelerar(self):
        print("El vehículo está acelerando")
    
    def frenar(self):
        print("El vehículo está frenando")
    
    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)

    vehiculo = Vehiculo("Toyota", "Corolla", 2020)
    vehiculo.acelerar()
    vehiculo.frenar()
    vehiculo.mostrar_informacion()
    ```    

 5. Crea una clase llamada "Banco" que tenga atributos de nombre y lista de clientes. Implementa métodos para agregar clientes, eliminar clientes y mostrar la lista de clientes.

    ```python
    class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
        else:
            print("El cliente no existe")
    
    def mostrar_clientes(self):
        print("Lista de clientes:")
        for cliente in self.clientes:
            print(cliente)

    banco = Banco("Mi Banco")
    banco.agregar_cliente("Juan")
    banco.agregar_cliente("María")
    banco.eliminar_cliente("María")
    banco.mostrar_clientes()
    ```

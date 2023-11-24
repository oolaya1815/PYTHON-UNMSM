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

6. Crea una clase Persona que tenga un constructor que reciba el nombre, la edad y el género de la persona. Crea dos clases hijas que hereden de Persona: Estudiante y Profesor. La clase Estudiante debe tener un atributo curso que indique el curso en el que está matriculado. La clase Profesor debe tener un atributo asignatura que indique la asignatura que imparte. Crea una clase TestPersona que tenga un método main que cree un array de Persona con tres elementos, uno de cada tipo de persona, e imprima los datos de cada una de ellas.

    ```python
    # Clase Persona
    class Persona:
        # Constructor que recibe el nombre, la edad y el género
        def __init__(self, nombre, edad, genero):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
        
        # Método que devuelve una representación de la persona como una cadena
        def __str__(self):
            return f"Persona: {self.nombre}, {self.edad} años, {self.genero}"
    
    # Clase Estudiante que hereda de Persona
    class Estudiante(Persona):
        # Constructor que recibe el nombre, la edad, el género y el curso
        def __init__(self, nombre, edad, genero, curso):
            # Llamada al constructor de la clase base
            super().__init__(nombre, edad, genero)
            self.curso = curso
        
        # Sobrescritura del método __str__
        def __str__(self):
            return f"Estudiante: {self.nombre}, {self.edad} años, {self.genero}, curso {self.curso}"
    
    # Clase Profesor que hereda de Persona
    class Profesor(Persona):
        # Constructor que recibe el nombre, la edad, el género y la asignatura
        def __init__(self, nombre, edad, genero, asignatura):
            # Llamada al constructor de la clase base
            super().__init__(nombre, edad, genero)
            self.asignatura = asignatura
        
        # Sobrescritura del método __str__
        def __str__(self):
            return f"Profesor: {self.nombre}, {self.edad} años, {self.genero}, asignatura {self.asignatura}"
    
    # Clase TestPersona que tiene el método main
    class TestPersona:
        def main():
            # Crear un array de Persona con tres elementos
            personas = [Persona("Ana", 25, "F"), Estudiante("Luis", 20, "M", "Matemáticas"), Profesor("Pedro", 35, "M", "Informática")]
            # Imprimir los datos de cada persona
            for persona in personas:
                print(persona)
    
    # Llamar al método main
    TestPersona.main()
    ```

8. Escriba una clase llamada Figura que tenga un atributo color y un método area que devuelva el área de la figura. Luego, escriba dos subclases llamadas Circulo y Rectangulo que hereden de Figura y sobreescriban el método area para calcular el área específica de cada figura. Finalmente, cree un objeto de cada subclase y muestre su área y color.


   ```python
   # Importar el módulo math para usar pi
   import math
   
   # Clase Figura
   class Figura:
       # Constructor con color
       def __init__(self, color):
           self.color = color
       
       # Método area que devuelve el área de la figura
       def area(self):
           return 0.0 # Por defecto, el área es cero
       
       # Método para obtener el color
       def get_color(self):
           return self.color
   
   # Clase Circulo que hereda de Figura
   class Circulo(Figura):
       # Constructor con color y radio
       def __init__(self, color, radio):
           # Llamada al constructor de la superclase
           super().__init__(color)
           self.radio = radio
       
       # Método area que sobreescribe el de la superclase
       def area(self):
           return math.pi * self.radio * self.radio # Fórmula del área del círculo
   
   # Clase Rectangulo que hereda de Figura
   class Rectangulo(Figura):
       # Constructor con color, base y altura
       def __init__(self, color, base, altura):
           # Llamada al constructor de la superclase
           super().__init__(color)
           self.base = base
           self.altura = altura
       
       # Método area que sobreescribe el de la superclase
       def area(self):
           return self.base * self.altura # Fórmula del área del rectángulo
   
   # Crear un objeto de la clase Circulo
   c = Circulo("azul", 5.0)
   # Mostrar el área y el color del círculo
   print("El área del círculo es " + str(c.area()))
   print("El color del círculo es " + c.get_color())
   
   # Crear un objeto de la clase Rectangulo
   r = Rectangulo("rojo", 10.0, 8.0)
   # Mostrar el área y el color del rectángulo
   print("El área del rectángulo es " + str(r.area()))
   print("El color del rectángulo es " + r.get_color())   
   ```
   
9. Escriba una clase llamada Empleado que tenga los atributos nombre, salario y antiguedad. Luego, escriba dos subclases llamadas Gerente y Vendedor que hereden de Empleado y tengan un atributo adicional llamado bono. El bono de un gerente es el 10% de su salario, mientras que el bono de un vendedor es el 5% de su salario más el 2% de sus ventas. Escriba un método sueldo_total que devuelva el salario más el bono de cada empleado. Finalmente, cree un objeto de cada subclase y muestre su sueldo total.

   ```python
   # Clase Empleado
   class Empleado:
       # Constructor con nombre, salario y antiguedad
       def __init__(self, nombre, salario, antiguedad):
           self.nombre = nombre
           self.salario = salario
           self.antiguedad = antiguedad
       
       # Método sueldo_total que devuelve el salario más el bono
       def sueldo_total(self):
           return self.salario + self.bono() # Suma el salario y el bono
       
       # Método bono que devuelve el bono del empleado
       def bono(self):
           return 0.0 # Por defecto, el bono es cero
       
       # Método para obtener el nombre
       def get_nombre(self):
           return self.nombre
   
   # Clase Gerente que hereda de Empleado
   class Gerente(Empleado):
       # Constructor con nombre, salario, antiguedad y bono
       def __init__(self, nombre, salario, antiguedad, bono):
           # Llamada al constructor de la superclase
           super().__init__(nombre, salario, antiguedad)
           self.bono = bono
       
       # Método bono que sobreescribe el de la superclase
       def bono(self):
           return self.bono # El bono es el 10% del salario
   
   # Clase Vendedor que hereda de Empleado
   class Vendedor(Empleado):
       # Constructor con nombre, salario, antiguedad, bono y ventas
       def __init__(self, nombre, salario, antiguedad, bono, ventas):
           # Llamada al constructor de la superclase
           super().__init__(nombre, salario, antiguedad)
           self.bono = bono
           self.ventas = ventas
       
       # Método bono que sobreescribe el de la superclase
       def bono(self):
           return self.bono + self.ventas * 0.02 # El bono es el 5% del salario más el 2% de las ventas
   
   # Crear un objeto de la clase Gerente
   g = Gerente("Ana", 3000.0, 5, 300.0)
   # Mostrar el sueldo total y el nombre del gerente
   print("El sueldo total de " + g.get_nombre() + " es " + str(g.sueldo_total()))
   
   # Crear un objeto de la clase Vendedor
   v = Vendedor("Luis", 2000.0, 3, 100.0, 5000.0)
   # Mostrar el sueldo total y el nombre del vendedor
   print("El sueldo total de " + v.get_nombre() + " es " + str(v.sueldo_total()))
   
   ```

10. Escriba una clase llamada Animal que tenga un atributo nombre y un método sonido que imprima el nombre y el sonido que hace el animal. Luego, escriba dos subclases llamadas Perro y Gato que hereden de Animal y sobreescriban el método sonido para imprimir el nombre y el sonido específico de cada animal. Finalmente, cree un objeto de cada subclase y muestre su sonido.

    ```Python
    # Clase Animal
    class Animal:
        # Constructor con nombre
        def __init__(self, nombre):
            self.nombre = nombre
        
        # Método sonido que imprime el nombre y el sonido del animal
        def sonido(self):
            print(self.nombre + " hace ...")
    
    # Clase Perro que hereda de Animal
    class Perro(Animal):
        # Método sonido que sobreescribe el de la superclase
        def sonido(self):
            print(self.nombre + " hace guau")
    
    # Clase Gato que hereda de Animal
    class Gato(Animal):
        # Método sonido que sobreescribe el de la superclase
        def sonido(self):
            print(self.nombre + " hace miau")
    
    # Crear un objeto de la clase Perro
    p = Perro("Firulais")
    # Mostrar el sonido del perro
    p.sonido()
    
    # Crear un objeto de la clase Gato
    g = Gato("Pelusa")
    # Mostrar el sonido del gato
    g.sonido()
    ```

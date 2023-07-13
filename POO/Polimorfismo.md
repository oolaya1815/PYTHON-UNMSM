# Polimorfismo

El polimorfismo es un concepto en la programación orientada a objetos (POO) que se refiere a la capacidad de un objeto para tomar diferentes formas y comportarse de diferentes maneras en función del contexto en el que se utilice.

En el contexto de la herencia, el polimorfismo se logra mediante el uso de métodos con el mismo nombre en diferentes clases. Estos métodos pueden tener implementaciones diferentes en cada clase, lo que permite que un objeto de una clase se comporte de manera distinta según su tipo concreto.

El polimorfismo permite escribir código más genérico y flexible, ya que se pueden utilizar variables y parámetros de tipos genéricos y aprovechar el comportamiento específico de cada objeto en tiempo de ejecución.

Por ejemplo, si tenemos una clase `Animal` con un método `hacer_sonido()`, y luego creamos subclases como `Perro` y `Gato` que heredan de la clase `Animal` y sobrescriben el método `hacer_sonido()`, podemos tener una lista de objetos de tipo `Animal` y llamar al método `hacer_sonido()` en cada objeto sin importar su tipo concreto. Cada objeto de la lista se comportará de acuerdo a su implementación específica del método `hacer_sonido()`.

El polimorfismo es una poderosa herramienta en POO que permite escribir código más flexible, modular y reutilizable, y facilita el diseño de programas orientados a objetos.

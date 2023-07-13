# Herencia

La herencia es un mecanismo en la programación orientada a objetos (POO) que permite que una clase herede atributos y métodos de otra clase. La clase que hereda se llama subclase o clase derivada, y la clase de la cual se heredan los atributos y métodos se llama superclase o clase base.

La herencia se define mediante la siguiente sintaxis:

```python
class Subclase(Superclase):
    # Definición de atributos y métodos adicionales de la subclase
    pass
```

La subclase tiene acceso a los atributos y métodos de la superclase, lo que permite la reutilización de código y la extensión de funcionalidades. La subclase puede agregar nuevos atributos y métodos, y también puede sobrescribir los atributos y métodos de la superclase para modificar su comportamiento.

Por ejemplo, si tenemos una superclase llamada `Animal` y una subclase llamada `Perro`, la subclase `Perro` puede heredar los atributos y métodos de la superclase `Animal`, como `nombre` y `hacer_sonido`. Además, la subclase `Perro` puede agregar atributos específicos de perros, como `raza`, y métodos adicionales, como `ladrar`.

La herencia nos permite crear jerarquías de clases y modelar relaciones entre objetos de manera más eficiente. También promueve la reutilización de código y facilita el mantenimiento y la extensión de nuestros programas.

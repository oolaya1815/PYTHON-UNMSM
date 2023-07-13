## Clase

Una clase es una plantilla o un molde que define la estructura y el comportamiento de los objetos. Define los atributos y métodos que los objetos de esa clase pueden tener.

### Definición de una clase

La sintaxis para definir una clase en Python es la siguiente:

```python
class MiClase:
    # Definición de atributos y métodos
    pass
```

### Atributos de clase

Los atributos de clase son variables que pertenecen a la clase en su conjunto y son compartidos por todos los objetos de esa clase. Se definen dentro de la clase pero fuera de cualquier método.

```python
class Persona:
    especie = "Humano"
    contador_personas = 0
```

En el ejemplo anterior, la clase Persona tiene dos atributos: especie y contador_personas. El atributo especie es una variable compartida por todas las instancias de la clase Persona, mientras que contador_personas es un contador que se incrementa cada vez que se crea una nueva instancia de Persona.

El ámbito de un atributo en Python se refiere a su visibilidad y accesibilidad desde diferentes partes del código. Los atributos pueden tener diferentes ámbitos según cómo se definen dentro de una clase.

- Atributos de instancia: Son aquellos atributos que se definen dentro de un método de la clase y están asociados a una instancia específica de esa clase. Estos atributos son accesibles a través de la instancia y su valor puede variar entre diferentes instancias de la misma clase.

- Atributos de clase: Son atributos que se definen dentro de la clase pero fuera de cualquier método. Estos atributos son compartidos por todas las instancias de la clase y tienen el mismo valor para todas ellas.

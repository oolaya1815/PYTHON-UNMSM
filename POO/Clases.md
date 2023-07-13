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

class Persona:
    especie = "Humano"
    contador_personas = 0

En el ejemplo anterior, la clase Persona tiene dos atributos: especie y contador_personas. El atributo especie es una variable compartida por todas las instancias de la clase Persona, mientras que contador_personas es un contador que se incrementa cada vez que se crea una nueva instancia de Persona.

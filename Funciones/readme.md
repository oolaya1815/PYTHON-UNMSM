# Funciones

## ¿Qué es una función?

Las funciones son una herramienta muy útil en programación que nos permiten escribir una porción de código que realiza una tarea específica y luego podemos usar esa porción de código una y otra vez en nuestro programa.

Imagina que estás haciendo un pastel. Para hacer un pastel, necesitas mezclar los ingredientes, colocarlos en un molde y meterlo en el horno. En programación, una función sería como una receta para hacer un pastel. Tú escribes una vez la receta y luego puedes usarla una y otra vez para hacer pastel.

En Python, para definir una función, debemos usar la palabra clave **"def"** seguida del nombre que le queremos dar a la función, luego los parámetros que necesita (que son como los ingredientes que necesita nuestra receta), y finalmente el cuerpo de la función, que es donde escribimos el código que queremos que haga la función.

Por ejemplo, aquí te muestro cómo podríamos definir una función para sumar dos números:

```
def suma(num1, num2):
  resultado = num1 + num2
  return resultado
```

Esta función se llama "suma" y recibe dos parámetros: "num1" y "num2". Luego, en el cuerpo de la función, se suman los dos números y se guarda el resultado en una variable llamada "resultado". Finalmente, se usa la palabra clave "return" para devolver el resultado de la suma.

Para usar esta función en nuestro programa, podemos llamarla y pasarle dos números como argumentos:

```
resultado = suma(3, 5)
print(resultado)
```

En este ejemplo, estamos llamando a la función "suma" y pasándole los números 3 y 5 como argumentos. La función realiza la suma y devuelve el resultado, que se guarda en una variable llamada "resultado". Luego, imprimimos el resultado en la pantalla.

## ¿Por qué usamos funciones?

Las funciones son una herramienta muy útil en programación por varias razones:

1.	Reutilización de código: una función es un bloque de código que realiza una tarea específica y se puede reutilizar en diferentes partes del programa. Al utilizar funciones, podemos escribir una vez un bloque de código para realizar una tarea específica y luego reutilizarlo en diferentes partes del programa sin tener que volver a escribirlo. Esto puede ahorrar tiempo y hacer que nuestro código sea más fácil de mantener.

2.	Modularidad: las funciones nos permiten dividir nuestro programa en módulos más pequeños y fáciles de entender. Cada función realiza una tarea específica, lo que hace que nuestro programa sea más fácil de leer y entender. Además, si se encuentra un error en una función, es más fácil encontrar y corregir ese error en lugar de tener que buscarlo en todo el programa.

3.	Abstracción: las funciones nos permiten abstraer los detalles de implementación de una tarea y concentrarnos en la tarea en sí. Esto nos ayuda a separar la lógica de la implementación y hacer nuestro código más claro y fácil de entender.

4.	Organización: las funciones nos ayudan a organizar nuestro código de una manera lógica y estructurada. Al dividir nuestro programa en funciones, podemos mantener nuestro código organizado y fácil de entender, lo que hace que sea más fácil trabajar en él y mantenerlo a largo plazo.

En resumen, las funciones son una herramienta esencial en programación que nos ayudan a escribir código más eficiente, modular y fácil de entender. Al utilizar funciones, podemos reutilizar código, hacer nuestro programa más fácil de leer y mantener, y dividir nuestro código en módulos más pequeños y manejables.
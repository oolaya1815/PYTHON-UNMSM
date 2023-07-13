# Conceptos de numeración

La numeración es un concepto fundamental en programación, ya que los programas manipulan constantemente números. Por lo tanto, es importante tener una comprensión sólida de los diferentes sistemas de numeración y cómo se utilizan en programación.

## Sistemas de numeración

En programación, se utilizan principalmente tres sistemas de numeración: el sistema decimal, el sistema binario y el sistema hexadecimal. Cada uno de estos sistemas de numeración tiene su propia base, que determina el número de símbolos que se utilizan y cómo se combinan para representar números.

### Sistema decimal

El sistema decimal es el sistema de numeración que utilizamos normalmente en nuestra vida cotidiana. Este sistema de numeración tiene una base de diez, lo que significa que utiliza diez símbolos (0-9) para representar números. En el sistema decimal, cada posición del número representa una potencia de diez.

Ejemplo: el número 456 en sistema decimal se representa como 4x10^2 + 5x10^1 + 6x10^0.

### Sistema binario

El sistema binario es el sistema de numeración utilizado por las computadoras para representar información digital. Este sistema de numeración tiene una base de dos, lo que significa que utiliza solo dos símbolos (0 y 1) para representar números. En el sistema binario, cada posición del número representa una potencia de dos.

Ejemplo: el número 101 en sistema binario se representa como 1x2^2 + 0x2^1 + 1x2^0, lo que da como resultado el número decimal 5.

### Sistema hexadecimal

El sistema hexadecimal es una notación de base 16 que se utiliza a menudo en programación para representar números binarios de una manera más compacta. En el sistema hexadecimal, se utilizan dieciséis símbolos (0-9 y A-F) para representar números. Cada dígito hexadecimal representa cuatro bits en el sistema binario.

Ejemplo: el número AB en sistema hexadecimal se representa como 10x16^1 + 11x16^0, lo que da como resultado el número decimal 171.

## Conversión entre sistemas de numeración

La conversión entre sistemas de numeración es una habilidad esencial para cualquier programador. La conversión entre el sistema binario y el sistema hexadecimal es particularmente importante, ya que estos sistemas de numeración se utilizan a menudo en la programación de computadoras.

### Conversión de binario a hexadecimal

Para convertir un número binario a hexadecimal, se divide el número binario en grupos de cuatro bits y se convierte cada grupo en su equivalente hexadecimal. A continuación, se combinan los dígitos hexadecimales para formar el número hexadecimal final.

Supongamos que tenemos el número binario 10100110. Para convertirlo a hexadecimal, primero debemos dividir el número binario en grupos de 4 dígitos, empezando por la derecha. Si el último grupo no tiene suficientes dígitos, se deben agregar ceros a la izquierda hasta completar los 4 dígitos.

1010 0110

Luego, convertimos cada grupo de 4 dígitos a su equivalente hexadecimal:

1010 0110 = A6

Por lo tanto, el número binario 10100110 es equivalente al número hexadecimal A6.

Es importante tener en cuenta que en el sistema hexadecimal, cada dígito representa un valor que va del 0 al 15. Los dígitos del 0 al 9 tienen el mismo valor que en el sistema decimal, mientras que los dígitos A, B, C, D, E y F representan los valores 10, 11, 12, 13, 14 y 15, respectivamente.

### Conversión de hexadecimal a binario

Para convertir un número hexadecimal a binario, se convierte cada dígito hexadecimal en su equivalente binario de cuatro bits. A continuación, se combinan los grupos de cuatro bits para formar el número binario final.

Supongamos que tenemos el número hexadecimal A6. Para convertirlo a binario, primero debemos convertir cada dígito hexadecimal a su equivalente binario de 4 dígitos. Para ello, podemos utilizar la siguiente tabla de conversión:

| Hexadecimal | Binario |
|-------------|---------|
| 0           | 0000    |
| 1           | 0001    |
| 2           | 0010    |
| 3           | 0011    |
| 4           | 0100    |
| 5           | 0101    |
| 6           | 0110    |
| 7           | 0111    |
| 8           | 1000    |
| 9           | 1001    |
| A           | 1010    |
| B           | 1011    |
| C           | 1100    |
| D           | 1101    |
| E           | 1110    |
| F           | 1111    |

Por lo tanto, el número hexadecimal A6 se puede representar en binario como:

A6 = 1010 0110

## Conclusiones

En resumen, la numeración es un concepto fundamental en programación. Los programadores deben estar familiarizados con los sistemas de numeración, cómo se utilizan en programación y cómo se convierten entre ellos. Con una comprensión sólida de estos conceptos, los programadores pueden trabajar con números de manera efectiva y eficiente, lo que es esencial en cualquier programa que involucre cálculo o manipulación de datos.

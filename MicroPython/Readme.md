MicroPython: Python para microcontroladoresMicroPython es una versión simplificada y optimizada de Python 3 que se puede ejecutar en microcontroladores, que son dispositivos electrónicos con poca memoria y potencia de procesamiento. MicroPython permite programar estos dispositivos de una forma fácil y divertida, usando un lenguaje de alto nivel y con una sintaxis clara y expresiva.
Características de MicroPythonMicroPython tiene las siguientes características principales:
- Es un lenguaje interpretado, lo que significa que el código se ejecuta directamente sin necesidad de compilarlo previamente. Esto facilita la depuración y el desarrollo interactivo.
- Soporta el paradigma de programación orientada a objetos, lo que permite crear y manipular entidades que tienen atributos y métodos que definen su comportamiento y estado.
- Tiene una biblioteca estándar que incluye módulos para realizar tareas comunes, como operaciones matemáticas, manejo de cadenas, archivos, etc. Algunos de estos módulos son versiones reducidas de los que existen en Python, y otros son específicos de MicroPython o de los microcontroladores que lo soportan.
- Tiene acceso directo al hardware del microcontrolador, lo que permite controlar los pines, los buses de comunicación, los sensores, etc. Para ello, se usan módulos como machine, esp o esp32, que ofrecen funciones y clases para interactuar con el hardware.
- Tiene un modo interactivo llamado REPL (Read-Eval-Print Loop), que permite escribir y ejecutar código en tiempo real, usando una consola o un navegador web. El REPL es muy útil para probar y experimentar con el lenguaje y el hardware.
Ventajas de MicroPythonMicroPython tiene las siguientes ventajas sobre otros lenguajes o entornos de programación para microcontroladores:
- Es fácil de aprender y de usar, ya que se basa en Python, uno de los lenguajes más populares y versátiles del mundo.
- Es portable y compatible, ya que se puede ejecutar en diferentes tipos de microcontroladores, como los basados en Arduino, ESP8266, ESP32, e Internet de las cosas .
- Es eficiente y rápido, ya que utiliza un compilador e intérprete optimizados para el bytecode de Python, que se ejecuta en el hardware del microcontrolador.
- Es abierto y colaborativo, ya que se trata de un proyecto de código abierto que cuenta con el apoyo de una gran comunidad de desarrolladores y usuarios.
Cómo empezar con MicroPythonPara empezar con MicroPython, se necesita lo siguiente:
- Un microcontrolador compatible con MicroPython, como el ESP32, que es una placa con un procesador de 32 bits, Wi-Fi, Bluetooth, y muchos pines y sensores.
- Un cable USB para conectar el microcontrolador al ordenador.
- Un editor de código o un IDE (Integrated Development Environment) que soporte MicroPython, como Thonny, Mu, uPyCraft, etc.
- Un firmware de MicroPython para el microcontrolador, que se puede descargar de la página oficial de MicroPython o de otras fuentes.
- Un programa para flashear el firmware en el microcontrolador, como esptool.py, que se puede instalar con pip.
Una vez que se tiene todo lo necesario, se puede seguir los siguientes pasos:
- Conectar el microcontrolador al ordenador con el cable USB.
- Ejecutar el programa de flasheo con los parámetros adecuados para el microcontrolador y el firmware.
- Abrir el editor de código o el IDE y seleccionar el puerto serie del microcontrolador.
- Escribir o cargar un código de MicroPython y ejecutarlo en el microcontrolador.
- Disfrutar de la programación con MicroPython.
Ejemplo de código de MicroPythonA continuación se muestra un ejemplo de código de MicroPython que hace parpadear un LED conectado al pin 2 del ESP32:

# Importar el módulo machine
import machine

# Crear un objeto Pin para el pin 2 en modo salida
pin = machine.Pin(2, machine.Pin.OUT)

# Crear un bucle infinito
while True:
    # Encender el pin
    pin.on()
    # Esperar medio segundo
    machine.time.sleep_ms(500)
    # Apagar el pin
    pin.off()
    # Esperar medio segundo
    machine.time.sleep_ms(500)
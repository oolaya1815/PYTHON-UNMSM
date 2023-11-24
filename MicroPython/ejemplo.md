# Ejemplos

1. Escriba un programa que encienda y apague un LED conectado al pin GPIO2 cada segundo, usando el módulo machine y el método sleep del módulo time.

    ```python
    # Importar el módulo machine
    import machine
    # Importar el método sleep del módulo time
    from time import sleep
    
    # Crear un objeto Pin para el pin GPIO2 en modo salida
    led = machine.Pin(2, machine.Pin.OUT)
    
    # Bucle infinito
    while True:
        # Encender el LED
        led.value(1)
        # Esperar un segundo
        sleep(1)
        # Apagar el LED
        led.value(0)
        # Esperar otro segundo
        sleep(1)
    ```
   
2.  Escriba un programa que lea la temperatura y la humedad de un sensor DHT11 conectado al pin GPIO4, usando el módulo dht y el método sleep del módulo time. El programa debe imprimir los valores leídos cada 5 segundos.

    ```python
    # Importar el módulo dht
    import dht
    # Importar el módulo machine
    import machine
    # Importar el método sleep del módulo time
    from time import sleep
    
    # Crear un objeto DHT11 para el pin GPIO4
    sensor = dht.DHT11(machine.Pin(4))
    
    # Bucle infinito
    while True:
        # Leer los datos del sensor
        sensor.measure()
        # Obtener la temperatura en grados Celsius
        temp = sensor.temperature()
        # Obtener la humedad en porcentaje
        hum = sensor.humidity()
        # Imprimir los valores leídos
        print("Temperatura: {} C, Humedad: {} %".format(temp, hum))
        # Esperar 5 segundos
        sleep(5)
    ```
3.  Escriba un programa que controle el brillo de un LED conectado al pin GPIO5 usando PWM (modulación por ancho de pulsos), usando el módulo machine y el método sleep del módulo time. El programa debe variar el ciclo de trabajo del PWM desde 0 hasta 1023 y luego desde 1023 hasta 0, creando un efecto de respiración.

    ```python
    # Importar el módulo machine
    import machine
    # Importar el método sleep del módulo time
    from time import sleep
    
    # Crear un objeto PWM para el pin GPIO5 con una frecuencia de 500 Hz
    led = machine.PWM(machine.Pin(5), freq=500)
    
    # Bucle infinito
    while True:
        # Bucle para aumentar el ciclo de trabajo desde 0 hasta 1023
        for duty in range(1024):
            # Establecer el ciclo de trabajo del PWM
            led.duty(duty)
            # Esperar 5 milisegundos
            sleep(0.005)
        # Bucle para disminuir el ciclo de trabajo desde 1023 hasta 0
        for duty in range(1023, -1, -1):
            # Establecer el ciclo de trabajo del PWM
            led.duty(duty)
            # Esperar 5 milisegundos
            sleep(0.005)
     ```  
4.   Escriba un programa que muestre un mensaje en una pantalla OLED de 128x64 píxeles conectada al ESP32 a través de I2C, usando el módulo ssd1306 y el módulo framebuf. El programa debe crear un objeto framebuf con un buffer de 128x64 bytes, dibujar el texto “Hola Mundo” en el buffer usando el método text, y luego enviar el buffer a la pantalla OLED usando el método show.

     ```python
      # Importar el módulo ssd1306
      import ssd1306
      # Importar el módulo framebuf
      import framebuf
      # Importar el módulo machine
      import machine
      
      # Crear un objeto I2C para el bus I2C0
      i2c = machine.I2C(0)
      # Crear un objeto SSD1306 para la pantalla OLED con dirección 0x3c
      oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)
      
      # Crear un buffer de 128x64 bytes
      buffer = bytearray(128 * 64 // 8)
      # Crear un objeto framebuf para el buffer con formato monocromo
      fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
      
      # Dibujar el texto "Hola Mundo" en el buffer con color blanco
      fb.text("Hola Mundo", 0, 0, 1)
      # Enviar el buffer a la pantalla OLED
      oled.blit(fb, 0, 0)
      # Mostrar el contenido de la pantalla OLED
      oled.show()
     ```
5.   Escriba un programa que envíe y reciba mensajes MQTT usando un broker público, usando el módulo umqtt.simple y el método sleep del módulo time. El programa debe conectarse al broker con un cliente ID único, suscribirse a un tópico llamado “esp32/test”, publicar un mensaje “Hello” en ese tópico cada 10 segundos, y mostrar en la consola cualquier mensaje que reciba en ese tópico.

     ```python
      # Importar el módulo umqtt.simple
      from umqtt.simple import MQTTClient
      # Importar el método sleep del módulo time
      from time import sleep
      
      # Definir el nombre del broker
      BROKER = "test.mosquitto.org"
      # Definir el puerto del broker
      PORT = 1883
      # Definir el cliente ID
      CLIENT_ID = "ESP32_123456"
      # Definir el tópico
      TOPIC = b"esp32/test"
      
      # Crear un objeto MQTTClient con el cliente ID y el broker
      client = MQTTClient(CLIENT_ID, BROKER, PORT)
      # Conectar al broker
      client.connect()
      # Suscribirse al tópico
      client.subscribe(TOPIC)
      
      # Definir una función para manejar los mensajes recibidos
      def on_message(topic, msg):
          # Imprimir el tópico y el mensaje
          print("Topic: {}, Message: {}".format(topic, msg))
      
      # Establecer la función on_message como callback del cliente
      client.set_callback(on_message)
      
      # Bucle infinito
      while True:
          # Publicar un mensaje "Hello" en el tópico
          client.publish(TOPIC, b"Hello")
          # Esperar 10 segundos
          sleep(10)
          # Verificar si hay mensajes pendientes
          client.check_msg()
     ```

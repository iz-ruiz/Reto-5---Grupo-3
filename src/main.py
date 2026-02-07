import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient

# CONFIGURACIÓN DE REQUISITOS 
MQTT_CLIENT_ID = "esp32-asir-cliente"
MQTT_BROKER    = "test.mosquitto.org"
MQTT_TOPIC     = "asir/grupo3/sensores" 

sensor = dht.DHT22(Pin(15)) 

# Conexión a la red Wokwi-GUEST
def conectar_wifi():
    print("Conectando a WiFi", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.1)
    print(" ¡Conectado!")

# Configuración Cliente MQTT
def conectar_mqtt():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
    client.connect()
    print("Conectado a Mosquitto")
    return client

conectar_wifi()
cliente = conectar_mqtt()

# Bucle de envío temporizado
while True:
    try:
        print("Midiendo...", end="")
        sensor.measure() # Lectura DHT22
        
        # Empaquetado en JSON
        payload = ujson.dumps({
            "temperatura": sensor.temperature(),
            "humedad": sensor.humidity(),
            "timestamp": time.time()
        })
        
        # Publicación en el topic exacto
        print(f"Enviando a {MQTT_TOPIC}: {payload}")
        cliente.publish(MQTT_TOPIC, payload)
        
    except OSError as e:
        print("Error al leer sensor.")
    
    time.sleep(10)

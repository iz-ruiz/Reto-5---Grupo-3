# Reto-5-Grupo-3
# Proyecto IoT: Monitorización Ambiental - Reto 5 (Fórmula 1)

## 📋 Descripción General
El presente proyecto tiene por objetivo el desarrollo de un sistema de monitorización de las condiciones de temperatura y humedad mediante la creación de una arquitectura de IoT que establece una conexión entre los dispositivos y las soluciones en la nube y locales. Se utiliza un microcontrolador ESP32 simulado en Wokwi, programado en MicroPython para realizar la captura de información del sensor DHT22 y enviarla en formato JSON utilizando el protocolo MQTT. La gestión de la información se distribuye en dos rutas: una visualización indirecta utilizando ThingSpeak en el cloud y un stack local gestionado con Docker Compose.

## 👥 Integrantes (Grupo 3)
* **Christian Manzambi** 
* **Mikel Gil** 
* **Izaro Ruiz** 
* **Jaime Iribarnegaray** 
* **Centro:** CPES San Luis LH BHIP 
* **Módulo:** Planificación y Administración de computación en la nube 
* **Curso:** 2º curso de ASIR, 2026 

---

## 🗺️ Mapa Lógico de la Red y Flujo de Datos
El sistema asegura la persistencia de la información y la supervisión de métricas ambientales a través del siguiente flujo de datos:

1. **Captura de Datos (Edge):** El proceso es ejecutado por un microcontrolador ESP32 que recoge lecturas de temperatura y humedad mediante un sensor DHT22 conectado al pin GPIO 15.
2. **Capa de Transporte (MQTT):** Se utiliza el protocolo MQTT por su ligereza y bajo consumo de ancho de banda. Los datos se empaquetan en JSON y se publican en el tópico `asir/grupo3/sensores` a través del broker `test.mosquitto.org`.
3. **Procesamiento Local (Node-RED):** En el entorno local, Node-RED intercepta los datos de MQTT y los redirige hacia la base de datos.
4. **Almacenamiento (InfluxDB):** Se utiliza InfluxDB para el almacenamiento histórico de los datos bajo la medición `clima_sensores`, asegurando el manejo eficiente de series temporales.
5.  **Visualización y Alertas (Grafana & ThingSpeak):**
    * **Local:** Grafana realiza la representación gráfica avanzada y gestiona el sistema de alertas ante condiciones críticas.
    * **Cloud:** ThingSpeak permite una visualización inmediata en la nube sincronizada a la base de datos sin infraestructura propia.

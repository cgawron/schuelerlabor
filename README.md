# Schülerlabor 2021 – Wetterstation mit ESP8266 & BME280
Wir bauen eine Wetterstation auf Basis eines ESP8266 Mikrocontrollers und eines [BME280 Sensors](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/).

## Installation Micropython
Dokumentation folgt.

## Auslesen der Sensorwerte
Dokumentation folgt.

## MQTT-Verbindung
Wir wollen die Daten nun "von außen" – also ohne USB-Verbindung zum ESP8266 Board – auslesen.
Die Idee ist folgende:
1. Wir verbinden den ESP8266 mit dem Internet. Dazu verwenden wir die WLAN-Schnittstelle des ESP8266 und verwenden uns mit einem Access-Point.
2. Wenn wir eine Verbindung zum Internet haben, senden wir die Daten über das [MQTT Protokoll](https://de.wikipedia.org/wiki/MQTT) an einen **MQTT Broker**.
   Für erste Tests verwenden wir dabei den öffentlichen Broker `broker.hivemq.com`.

Dafür benötigen wir zwei Dateien:
- Die Datei `umqttsimple.py` implementiert das MQTT-Protokoll,
- Die Datei `client.py` verbindet sich mit dem Broker und sendet testweise jede Sekunde eine Nachricht an den Broker.

## Anzeige der Nachrichten
Zum Anzeigen der Nachrichten verwenden wir zunächst den [MQTT Browser Client](http://www.hivemq.com/demos/websocket-client/).
![](https://www.hivemq.com/img/mqtt-websocket-client.gif)

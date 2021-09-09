import paho.mqtt.client as mqtt
import random
import time

topic = "teste"
host = "127.0.0.1"
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect() -> mqtt:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao MQTT")
        else:
            print("Desconectado!")
    
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(host,port)

    return client

def subscribe(client: mqtt):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}`topic")
    
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()
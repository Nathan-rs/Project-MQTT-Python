import paho.mqtt.client as mqtt
import random
import time


topic = "teste"
host = "127.0.0.1"
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao MQTT")
        else:
            print("Desconectado!")

    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(host,port)
    
    return client


def publish(client):
    cont = 0
    while True:
        time.sleep(2)
        msg = f"message: {cont}"
        result = client.publish(topic,msg)

        print(result)

        #result = [0 , 1]
        status = result[0]

        if status == 0:
            print(f"send `{msg}` to topic `{topic}`")
        else:
            print(f"Falied to send message to topic {topic}")
        
        cont = cont+1

def run():
    client = connect()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
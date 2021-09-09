import paho.mqtt.client as mqtt
import random
import time
import base64
from PIL import Image
from io import BytesIO
import cv2 as cv

topic = "teste"
topic_img = "teste/img"
host = "127.0.0.1"
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
contador = f'img/imagem-{random.randint(0, 1000)}'

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
    img_msg = None
    def on_message(client, userdata, msg):
        print("Messagem: ",msg.payload.decode(), " recebida no topico: ",msg.topic)
        img_msg = str(msg.payload.decode())
        image_show(img_msg)


        # print(image_decode(img))
        # img_base64 = image_decode(img)
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}`topic")
    
    client.subscribe(topic,2)
    client.on_message = on_message

def image_show(img):
    image = base64.b64decode(img)
    im = Image.open(BytesIO(base64.b64decode(img)))
    im.save(f'img/imagem-{random.randint(0, 1000)}.png', 'PNG')

def run():
    client = connect()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    try:
        run()
    except:
        print("Conexao interrompida!")
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

lista = []

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
        print("Messagem: nova imagem recebida no topico: ",msg.topic)
        img_msg = str(msg.payload.decode())
        image_show(img_msg)
    
    client.subscribe(topic,2)
    client.on_message = on_message

def image_show(img):
    image = base64.b64decode(img)
    im = Image.open(BytesIO(base64.b64decode(img)))
    name_image = f'img/imagem-{random.randint(0, 1000)}.png'
    im.save(name_image, 'PNG')
    lista.append(name_image)

def run():
    client = connect()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    try:
        run()
    except:
        print("Conexao interrompida!")
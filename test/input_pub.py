import paho.mqtt.client as mqtt
import random
import time
import json
import base64

topic = "teste"
topic_img = "teste/img"
host = "127.0.0.1"
port = 1883
client_id = ""


def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao MQTT")
        else:
            print("Desconectado!")


    nome = input("Informe o nome: ")

    if nome == "":
        client_id = f'python-mqtt-{random.randint(0, 1000)}'
    else:
        client_id = nome

    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(host,port)
    print("Cliente :", client_id, "conectado!")
    
    return client


def menu_publish():
    print("|-------------------------------------|")
    print("| 1 - Informar uma mensagem no topico-|")
    print("| 2 - Mandar um arquivo no topico-----|")
    print("| 0 - Sair ---------------------------|")
    print("|-------------------------------------|")
    op = int(input("> "))

    return op



def teste():
    with open("Bandeira_Alemanha.png", "rb") as image_file:
        image_string = base64.b64encode(image_file.read())

    return image_string

def numero():
    return 1

def publish_topic():
    print("Onde gostaria de publicar a mensagem?")
    print("|-------------------------------------|")
    print("| 1 - topico teste--------------------|")
    print("| 2 - topico teste/image--------------|")
    print("|-------------------------------------|")
    op = int(input("> "))
    return op

def publish(client):
    msg = ""
    result = 1
    op = menu_publish()

    while op != 0:
        # time.sleep(2)

        if op == 1:
            msg = input("Informe a mensagem: ")
        else:
            if op == 2:
                msg = teste()

        t_public = publish_topic()

        if t_public == 1 or t_public == None:
            result = client.publish(topic,msg)
        else:
            result = client.publish(topic_img, msg)
        
        #result = [0 , 1]
        status = result[0]
        
        if status == 0 and t_public == 1:
            print(f"\nMensagem enviada para o topico `{topic}`\n")
        else:
            if status == 0 and t_public == 2:
                print(f"\nMensagem enviada para o topico `{topic_img}`\n")
            else:
                print(f"Falha ao enviar a mensagem para o topico {topic_img}")

        
        op = menu_publish()
    client.disconnect()

def run():
    client = connect()
    # client.loop_start()
    publish(client)
    client.loop_start()

if __name__ == '__main__':
    # try:
        run()
    # except:
    #     print("Conexao interrompida!")
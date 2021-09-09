from tkinter import *
from tkinter import filedialog as fd
import input_pub as ip_pub
import interface_msg as im
import paho.mqtt.client as mqtt
import random
import base64

height = 300
width = 400

topic = "teste"
topic_msg = "teste/msg"
host = "127.0.0.1"
port = 1883
client_id = ""
# client = None

#varivale que contem o caminho das imagens no explorador de arquivos
img = ""
# message_var = None

def show_window(main):
    #pegando a resolucao da tela computador, no meu caso: 1366x768
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    #posicionamento da janela no centro
    posX = screen_width/2 - width/2
    posY = screen_height/2 - height/2

    #dimensao da tela
    main.geometry("%dx%d+%d+%d" % (width, height, posX, posY))
    main.resizable(False, False)

    #name windows
    main.title("Escolher Broker")

def Testando_components(main):

    label_title = Label(main, text="Escolha a opcao de broker")

    lable_broker_msg = Label(main, text="Broker Message: ")
    # lable_broker_msg.pack()
    # lable_broker_msg.place(x=100,y=10)

    lable_broker_img = Label(main, text="Broker Image: ")
    # lable_broker_img.pack()
    # lable_broker_img.place(x=100,y=80)

    btn_msg = Button(main,text="connect")
    btn_img = Button(main,text="connect")

    # btn_msg.pack()
    # btn_img.pack()

    # btn_msg.place(x=200,y=10)
    # btn_img.place(x=200,y=80)

    label_title.grid(row=0, column=0,columnspan=5)

    lable_broker_msg.grid(row=1, column=0,padx=10,pady=20)
    btn_msg.grid(row=1, column=1)

    lable_broker_img.grid(row=2,column=0,padx=10,pady=20)
    btn_img.grid(row=2,column=1)

def connect():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado ao MQTT")
        else:
            print("Desconectado!")

    client_id = f'python-mqtt-{random.randint(0, 1000)}'  
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.connect(host,port)
    print("Cliente :", client_id, "conectado!")
    
    return client

def img64():
    with open(img, "rb") as image_file:
        img_string = base64.b64encode(image_file.read())
    
    return img_string

# def publish(client):
    msg = img_base64

    result = client.publish(topic, msg)
        
    #result = [0 , 1]
    status = result[0]

    if status == 0:
        print(f"\nMensagem enviada para o topico `{topic}`\n")
    else:
        print(f"Falha ao enviar a mensagem para o topico {topic}")
        
    # client.disconnect()


def broker_msg():
    client = connect()
    b_msg = Toplevel()

    b_msg.title("Broker Message")
    b_msg.geometry("400x300+500+200")

    #titulo do painel
    Label(b_msg, text="Painel de mensagem", font=('calibre',14,'bold')).grid(row=0,column=0, sticky=W,columnspan=4)

    #campo de mensage
    Label(b_msg, text="mensagem: ").grid(row=1,column=0,padx=10,pady=30)
    message_entry = Entry(b_msg)
    message_entry.grid(row=1, column=1,padx=20,pady=10)
    
    #botao de enviar
    Button(b_msg, text="Enviar", command=lambda:submit_msg(message_entry)).grid(row=1, column=2)
    
    #mensagem de envio
    Label(b_msg, text="").grid(row=2,column=0)

    # submit_msg(message_entry)

    result = client.publish(topic_msg, message_entry.get(), 2)

    status = result[0]

    if status == 0:
        print("Mensagem enviada com sucesso ao topico :",topic_msg)
    else:
        print("Erro ao enviar a mensagem!")

    client.loop_start()

def submit_msg(message):
    print(message.get())

def open_image():
    #config de explorador de arquivo
    filetypes = (
        ('text files', '*.png'),
        ('All files', '*.*')
    )
    
    file_diretory = fd.askopenfilename(
        title="open file",
        initialdir='/',
        filetypes=filetypes
    )
    global img

    img = file_diretory


def public():
    msg = img64()

    print(msg)
    print(client_id)

    client = connect()

    result = client.publish(topic, msg, 2)

    status = result[0]

    if status == 0:
        print(f"\nMensagem enviada para o topico `{topic}`\n")
    else:
        print(f"Falha ao enviar a mensagem para o topico {topic}")

    client.loop_start()

def broker_img():
    
    b_img = Toplevel()
    b_img.title("Broker Image")
    b_img.geometry("500x300+450+150")

    Label(b_img, text="Painel de controle de Image").grid(row=0, column=0,sticky=W)
    Label(b_img, text="Open image: ").grid(row=1,column=0,padx=10,pady=10)
    Button(b_img, text="Abrir", command=open_image).grid(row=1, column=1, padx=10, pady=20)
    Button(b_img, text="Enviar",command=public).grid(row=2, column=0, sticky=EW)
    

def Init(main):

    #confg da grid
    main.columnconfigure(0,weight=0)
    main.rowconfigure(1, weight=0)

    Label(main, text="Escolha o Broker de publicador!").grid(row=0,column=1,sticky=N)
    
    Label(main, text="Broker Message: ").grid(row=1, column=1,padx=10,pady=20)
    Button(main, text="connect",command=broker_msg).grid(row=1,column=2)

    Label(main, text="Broker Image: ").grid(row=2, column=1,padx=10,pady=20)
    Button(main, text="connect",command=broker_img).grid(row=2,column=2)

#funcao main
if __name__ == '__main__':
    main = Tk()
    show_window(main)
    Init(main)
    main.mainloop()
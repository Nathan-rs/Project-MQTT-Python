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
host = "127.0.0.1"
port = 1883
client_id = ""

#varivale que contem o caminho das imagens no explorador de arquivos
img = ""

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

def components(main):

    label_title = Label(main, text="Escolha a opcao de broker")

    lable_broker_img = Label(main, text="Broker Image: ")
    
    lable_broker_img.pack()
    lable_broker_img.place(x=100,y=80)

    
    btn_img = Button(main,text="connect")

    label_title.grid(row=0, column=0,columnspan=5)

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

    Label(b_img, text="Painel de controle de Postagem", font=('calibre',14,'bold')).place(x=110,y=10)
    Label(b_img, text="Open image: ",font=('calibre',12,'bold')).place(x=100,y=150)
    btn_open = Button(b_img, text="Abrir", command=open_image,width=10).place(x=250,y=150)
    bnt_submit = Button(b_img, text="Enviar",command=public,width=10).place(x=350,y=150)

def Init(main):

    lbl_title = Label(main, text="Painel do publicador!", font=('calibre',14,'bold')).place(x=110,y=10)

    lbl_view = Label(main, text="Publicar postagem: ",font=('calibre',10,'bold')).place(x=65,y=150)
    
    bnt_view = Button(main, text="connect",command=broker_img,width=15).place(x=220, y=145)

#funcao main
if __name__ == '__main__':
    main = Tk()
    show_window(main)
    Init(main)
    main.mainloop()
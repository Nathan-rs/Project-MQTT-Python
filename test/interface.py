from tkinter import *

height = 400
width = 500

def connect_mqtt():
    print("Hellow Word!")

def Init(main):
    main.title("Primeira janela")
    
    #pegando a resolucao da tela computador, no meu caso: 1366x768
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    #posicionamento da janela no centro
    posX = screen_width/2 - width/2
    posY = screen_height/2 - height/2

    #dimensao da tela
    main.geometry("%dx%d+%d+%d" % (width, height, posX, posY))
    main.resizable(False, False) #não deixa redimensionar a tela

    #botoes
    btn_connect = Button(main, text="Connect", command = connect_mqtt)
    btn_connect.pack()
    btn_connect.place(x=440,y=5) #position buttons

def components(main):
    label_


if __name__ == '__main__':
    main = Tk()
    Init(main)
    main.mainloop()
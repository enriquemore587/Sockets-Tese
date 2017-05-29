import sys
from Tkinter import *
import time
import sockets as client
import sockets2 as ser
import thread
mensajeGlobal = None
obj = None
hola = '''<?xml version="1.0" encoding="utf-8"?>
<raiz>
<msg dispositivo="DISPOSITIVO ZORIN">
  HOLA
</msg>
</raiz>
'''
adios = '''<?xml version="1.0" encoding="utf-8"?>
<raiz>
<msg dispositivo="DISPOSITIVO ZORIN">
  ADIOS
</msg>
</raiz>
'''
def createXML(data):
    try:
        file = open('entrada.xml', "w")
        file.writelines(data)
        file.close()
        return True
    except:
        return False

def readXML():
    from lxml import etree
    try:
        doc = etree.parse('entrada.xml')
        raiz=doc.getroot()
        print raiz.tag
        libro=raiz[0]
        return (libro.text.replace(" ", "").replace("\n", "").upper(), libro.attrib["dispositivo"].upper())
    except:
        return ('NO ES UN "XML o la primer linea esta en blanco"',"ERROR: " )
def iniciar():
    thread.start_new_thread(startServer, (12,))
def startServer(msg):
    try:
        obj = ser.sockets()
        obj.listen(host='', port=12345)
        while True:
            valor = obj.inMsg()
            if createXML(valor):
                print True
                cont, orig = readXML()
                print cont, orig
                if cont == "ADIOS":
                    lblStatus.config(text="%s %s DIJO: \n  %s      -       EL PUERTO SE ABRIRA DE NUEVO" % (orig, obj.addr, cont))
                    obj.closeSocket()
                    return
                else:
                    lblStatus.config(text="%s %s dice: \n  %s" % (orig, obj.addr, cont))
                    obj.outMsg(valor)
                    obj.closeSocket()
                    return
            else:
                print "no se creo el XML"
    except:
        msg = msg - 1
        print "lIBERANDO PUERTO EN %d. . ."% msg
        time.sleep(5)
        startServer(msg)

def conectar():
    _valor = combo.get()
    lblStatus.config(text='Estableciendo conexion con "%s" . . . '%_valor)
    client.conectar("localhost", 12345)
    time.sleep(1)
    lblStatus.config(text='Conexion establecida correctamente con "%s" . . . ' % _valor)

def saludar():
    _valor = combo.get()
    lblStatus.config(text='Saludo mandado a "%s" . . . ' % _valor)
    if createXML(client.enviar_msg(hola)):
        cont, orig = readXML()
        print cont, orig
        if cont == "ADIOS":
            lblStatus.config(text="%s DIJO: \n  %s      -      LA CONEXION TERMINO" % (orig, cont))
            client.cerrar()
            return
        else:
            lblStatus.config(text="%s dice: \n  %s" % (orig, cont))
            return
    else:
        print "no se creo correctamente el XML"

def despedir():
    _valor = combo.get()
    lblStatus.config(text='Adios Enviado \nconexion con "%s" deshabilitada ' % _valor)
    client.enviar_msg(adios)

# Primer ventana con valores positivos
ventana = Tk()
ventana.geometry("600x200+100+100")
# A modo estetico le di un titulo
ventana.title("SOCKETS SISTEMAS DISTRIBUIDOS")
# Este tambien es estetico y no influye en el uso del metodo
etiqueta = Label(ventana, text="Dispositivo con Python", width=100, height=0, anchor="center")
etiqueta.pack()
lblDisp = Label(ventana, text="Dispositivo ").place(x=100,y=50)
combo = Spinbox(ventana)
combo["values"] = ("Dispositivo A","Dispositivo B","Dispositivo C","Dispositivo D","Dispositivo E")
combo.place(x=200,y=50)
btn = Button(ventana, text= "CONECTAR", command= conectar).place(x=400, y=50)
btn2 = Button(ventana, text= "SALUDAR", command = saludar).place(x=150, y=100)
btn3 = Button(ventana, text= "DESPEDIR",command = despedir).place(x=400, y=100)
lblStatus = Label(ventana,text="Status. . . ")
lblStatus.pack()
btnStartServer = Button(ventana, text= "Start", command= iniciar).place(x=530, y=150)
ventana.mainloop()


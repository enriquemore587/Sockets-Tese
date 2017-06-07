import socket
import thread

class startHotel(object):
    soc = None
    addr = None
    conn = None
    host = None
    port = None

    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            print "No se pudo instanciar el sockket"

        print "Server Iniciado \n esperando cliente. . . ."
        try:
            self.soc.bind((self.host, self.port))
            self.soc.listen(1)
            self.conn, self.addr = self.soc.accept()
            print ("Got connection from", self.addr)
        except:
            print 'No se puede iniciar Server en el puerto: %s' % (port)

    def inMsg(self):
        msg = self.conn.recv(1024).decode()
        return msg

    def outMsg(self, msg):
        self.conn.sendall(msg)
        print ('enviado !')

    def closeSocket(self):
        self.soc.close()
        self.conn.close()

def createXML(data):
    try:
        file = open('input.xml', "w")
        file.writelines(data)
        file.close()
        return True
    except:
        return False

import Trata
def readXML():
    from lxml import etree
    try:
        doc = etree.parse('input.xml')
        raiz=doc.getroot()
        atributo = raiz
        return atributo.get("nivel")
    except:
        return ('NO ES UN "XML o la primer linea esta en blanco"',"ERROR: " )
if __name__ == '__main__':
    server1 = startHotel(port=12345, host='localhost')
    createXML(server1.inMsg())
    inn = readXML()
    if inn == 'login':
        print "Es un Login"
    elif inn == "getHotel":
        print "Pide hoteles"
    elif inn == "getHabitaciones":
        print "solicita Habitaciones"
    elif inn == "requestHabitacion":
        print "solicita Habitaciones"
    elif inn == "confirmHabitacion":
        print "Confirma habitacion"

import socket
class sockets(object):
    soc = None
    addr = None
    conn = None
    host = None
    port = None
    def listen(self, host, port):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host; self.port = port
        self.soc.bind((self.host, self.port))
        self.soc.listen(1)
        print "Server Iniciado \n esperando cliente. . . ."
        self.conn, self.addr = self.soc.accept()
        print ("Got connection from",self.addr)
    def inMsg(self):
        host, port = self.addr
        msg = self.conn.recv(1024).decode()
        return msg

    def outMsg(self, msg):
        self.conn.sendall(msg)
        print ('enviado !')
    def closeSocket(self):
        self.soc.close()
        self.conn.close()

'''while True:
    input = obj.inMsg()
    if input == "bye":
        break
    obj.outMsg("I'm Python")
obj.closeSocket()'''

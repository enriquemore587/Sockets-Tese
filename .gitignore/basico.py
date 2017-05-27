'''
Author: https://github.com/enriquemore587
'''
import socket

soc = socket.socket()
host = "localhost"; port = 5552
soc.bind((host, port))
soc.listen(5)

conn, addr = soc.accept()
print ("Got connection from",addr)

msg = conn.recv(1024)
print msg
host, port = addr
msg = 'Tu mensaje fue recibido correctamente %s ' % str(host)
print msg
conn.sendall(msg)
print 'enviado !'

conn.close()
soc.close()

#!/usr/bin/env python
# author https://github.com/enriquemore587

# importamos el modulo para trabajar con sockets
import socket

# Creamos un objeto socket para el servidor. Podemos dejarlo sin parametros pero si
# quieren pueden pasarlos de la manera server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket()

# Nos conectamos al servidor con el metodo connect. Tiene dos parametros
# El primero es la IP del servidor y el segundo el puerto de conexion


# Creamos un bucle para retener la conexion
def conectar(host, port):
    s.connect((host, port))
def enviar_msg(mensaje):
    s.send(mensaje)
    c = recibir()
    return c
def recibir():
    recibido = s.recv(1024)
    return recibido
def cerrar():
    # Cerramos la instancia del objeto servidor
    s.close()

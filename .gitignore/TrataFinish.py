#!/usr/bin/env python
# -*- coding: utf-8 -*-
import conexion as cn
def crearXML(data):
    try:
        file = open('archivo.xml', 'w')
        file.writelines(data)
        file.close()
        print 'Creado exitosamente'
    except:
        print "No se puede Crear el archivo con los datos. . . \n", data

def login(data):
    crearXML(data)

    from lxml import etree
    xml = etree.parse("archivo.xml")
    raiz = xml.getroot()
    userName = raiz[0].text
    con= raiz[0].attrib["pwd"]

    dataUser = {
        "usr": userName,
        "pwd": con
    }
    resp = cn.login(dataUser)
    if resp != None:
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="login"><usr name="%s">%s</usr></raiz>' % (resp['name'], resp['usr'])
        return data
    else:
        return False

#data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="login"><usr pwd="XXXXXXX">JOSE123</usr></raiz>'
#print login(data)

#--------------------------------------------------------
def requestHabitacion(data):
    crearXML(data)
    from lxml import etree
    xml = etree.parse("archivo.xml")
    #ruta,habitacion,tipo,start
    raiz = xml.getroot()
    habitacion = raiz[0]
    tipo = habitacion[0].text
    cant = habitacion[1].text
    dateI = habitacion[2].text
    dateO = habitacion[3].text
    Usr = habitacion[4].text
    print tipo
    print cant
    print dateI
    print dateO
    print Usr

    data ={
     "tipo" :tipo,
     "cantidad" : cant,
     "dateIn": dateI,
     "dateOut": dateO,
     "user": Usr
    }

    resp = cn.requestHabitacion(data)
    if resp != 1 and resp != 2:
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="requestHabitacion"><userBanco>%s</userBanco><cantidad>%s</cantidad></raiz>' % (
        resp["userBanco"], resp['precio'])
        return data
    else:
        return  resp#1 o 2



data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="requestHabitacion"><habitacion><tipo>STAR</tipo><cantidad>3</cantidad><dateIn>2016-05-05</dateIn><dateOut>2016-05-15</dateOut><user>JOSE123</user></habitacion></raiz>'
#requestHabitacion(data)



def getHotel(nameCity):
    crearXML(data=nameCity)
    from lxml import etree
    xml = etree.parse("archivo.xml")
    raiz = xml.getroot()
    city = raiz[0].text
    diccionario = {
        'nameCity' : city
    }
    hoteles = cn.getHotel(nameCity= diccionario)

    xml = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHotel">'
    for hotel in hoteles:
        h = hotel['hotel']
        c = hotel['calificacion']
        xml = xml + '<hotel clasificacion="%s">%s</hotel>' % (c, h)
    xml = xml + '</raiz>'
    return xml


#nameCity = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHotel"><ciudad>MONTERREY</ciudad></raiz>'
#getHotel(nameCity)



    #hoteles es la variable que regresa el metodo - esto es un arreglo......



def getHabitaciones(data):
    crearXML(data)
    from lxml import etree
    xml = etree.parse("archivo.xml")
    raiz  = xml.getroot()
    Hotel = raiz[0].text
    habitaciones = cn.getHabitaciones(Hotel)

    xml = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHabitaciones">'

    for item in habitaciones:
        tipo = str(item['tipo'])
        disponibles = str(item['disponibles'])
        precio = str(item['precio'])
        xml = xml + '<habitacion precio="%s">%s<disponibles>%s</disponibles></habitacion>' % (precio, tipo, disponibles)
    xml = xml + '</raiz>'
    return xml


data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHabitaciones"><hotel>nombre del hotel</hotel></raiz>'
#print getHabitaciones(data)



def confirmHabitacion(data):
    crearXML(data)
    from lxml import etree
    xml = etree.parse('archivo.xml')
    raiz = xml.getroot()
    banco = raiz[0].text
    res = raiz[1].text

    data = {
         "usrBanco": banco,
         "res": res
    }

    resp = cn.confirmHabitacion(data)
    if resp['res'] == 'true':
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="confirmHabitacion"><resp>%s</resp></raiz>' % 'true'
        return (data)
    else:
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="confirmHabitacion"><resp>false</resp></raiz>'
        return (data)


data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="confirmHabitacion"><usrBanco>JOSE21JOSE</usrBanco><resp>true</resp></raiz>'
print confirmHabitacion(data)


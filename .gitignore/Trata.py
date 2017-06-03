def login(data):
    '''
    :param data:
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="login"><usr pwd="XXXXXXX">JOSE123</usr></raiz>'
    :return:
        data = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="login"><usr name="JOSE ENRIQUE VERGARA AMBRIZ">JOSE123</usr></raiz>'
    '''
    pass

def getHotel(nameCity):
    '''
    :param nameCity: '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHotel"><ciudad>MONTERREY</ciudad></raiz>'
    :return:
     hoteles = '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHotel"><hotel clasificacion="5 Estrellas">hotel 1</hotel><hotel clasificacion="4 Estrellas">hotel 2</hotel><hotel clasificacion="3 Estrellas">hotel 3</hotel></raiz>'
    '''
    #entra nombre de la ciudad
    #retorna un arreglo con todos los nombres de los hoteles existentes
    pass
def getHabitaciones(nameHotel):
    # entra nombre del hotel
    # retorna un arreglo de diccionarios de los tipos de habitaciones y cantidad de estas disponibles con el precio
    # con el formato
    '''
    :param nameHotel:
        '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHabitaciones"><hotel>nombre del hotel</hotel></raiz>'
    :return:
        '<?xml version="1.0" encoding="utf-8"?><raiz nivel="getHabitaciones"><habitacion precio="2500.50">STAR<cantidad>6</cantidad></habitacion><habitacion precio="1500.50">GOLDEN<cantidad>16</cantidad></habitacion><habitacion precio="500.00">CLASIC<cantidad>2</cantidad></habitacion></raiz>'
    '''
    pass
def requestHabitacion(data):
    '''
    :param data:
    '<?xml version="1.0" encoding="utf-8"?><raiz nivel="requestHabitacion"><habitacion><tipo>STAR</tipo><cantidad>3</cantidad><dateIn>2016-05-05</dateIn><dateOut>2016-05-15</dateOut><user>JOSE123</user></habitacion></raiz>'
    :return:
    '<?xml version="1.0" encoding="utf-8"?><raiz nivel="requestHabitacion"><userBanco>JOSE21JOSE</userBanco><cantidad>100000</cantidad></raiz>'
    '''
    pass
def confirmHabitacion(data):
    '''
    :param data:
     '<?xml version="1.0" encoding="utf-8"?><raiz nivel="confirmHabitacion"><usrBanco>JOSE21JOSE</usrBanco><resp>True</resp></raiz>'
    :return:
    '<?xml version="1.0" encoding="utf-8"?><raiz nivel="confirmHabitacion"><resp>True</resp></raiz>'
    '''
    pass
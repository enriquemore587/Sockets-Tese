def login(dataUser):
    '''
    :param dataUser:
     dataUser = {
        usr: 'userName',
        pwd: 'XXXXXXX'
     }
    :return:
    si existe en la bd
    datosUsuario = {
        name: 'JOSE ENRIQUE VERGARA AMBRIZ',
        usr: 'JOSE123'
    }
    si no
    None
    '''
    pass

def getHotel(nameCity):
    '''
    :param nameCity: 'GUERRERO'
    :return:
     hoteles = [
        {
            nameHotel: 'Hotel 1',
            calificacion: '5 Estrellas'
        }
     ]
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
     'Hotel 1'
    :return:
        habitaciones = [
            {
                tipo: 'Star',
                disponibles: 6,
                precio: 2500.50
            },
            {
                tipo: 'Golden',
                disponibles: 19,
                precio: 1500.00
            },
            {
                tipo: 'Clasic',
                disponibles: 2,
                precio: 500.50
            }
        ]
    '''
    pass
def requestHabitacion(data):
    '''
    :param data:
    data = {
        tipo: 'STAR',
        cantidad: 2,
        dateIn: '2016-05-05',
        dateOut: '2016-07-15'
        user: 'JOSE123'
    }
    :return:
    userBanco = 'JOSE21JOSE'
    '''
    pass
def confirmHabitacion(data):
    '''

    :param data:
     data = {
        usrBanco: 'JOSE21JOSE',
        resp: True  #or False
     }
    :return:
    True - False
    '''
    pass
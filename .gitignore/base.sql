--Create database Hotel;
use Hotel;

create table usuarios
(
id int primary key identity,
nombre varchar(15),
aPaterno  varchar(15),
aMaterno varchar(15),
usr varchar(15),
usrBanco varchar(15),
pwd varchar(15)
);

insert into usuarios values('Jose Enrique', 'Vergara', 'Ambriz', 'more', 'more123', '123');
insert into usuarios values('Edgar Rogelio', 'Mancilla', 'Garcia', 'venga', 'venga123', '123');
go

select CONCAT(nombre, ' ',aPaterno, ' ',aMaterno )as name  from usuarios where usr = 'more' and pwd = '123';
select distinct nombre from ciudades
create table ciudades
(
	id int primary key identity,
    nombre varchar(50)
);
insert into ciudades values ('CANCUN') 
insert into ciudades values ('MONTERREY') 
insert into ciudades values ('MEXICO') 
insert into ciudades values ('PUEBLA') 
insert into ciudades values ('VALLE DE BRAVO') 

create table hoteles
(
	id int primary key identity,
    nombre varchar(50),
	clasificacion varchar(30),
    ciudad int references ciudades (id)
);

select nombre, clasificacion from hoteles where ciudad = (select id from ciudades where nombre ='CANCUN')
insert into hoteles values('Hotel Super More','5 ESTRELLAS', 1);
insert into hoteles values('Hotel mini super More','3 ESTRELLAS', 1);

create table habitaciones
(
	id int primary key identity,
    tipo varchar(50),
    precio float,
    numero int,
    hotel int references hoteles (id)
);
select tipo, numero, precio from habitaciones where hotel = (select id from hoteles where nombre ='Hotel Super More')
insert into habitaciones values ('Lujo', 5000.00, 5, 1);
insert into habitaciones values ('Sencilla', 2000.00, 34, 1);
insert into habitaciones values ('Golden',8000.00, 9, 1);
go

create table reservas
(
	idHotel int references hoteles (id),
    idHabitacion int references habitaciones(id),
    datein date,
    dateout date,
    cantidad int,
	cinfirmacion int default 0
);

select * from reservas
select id from habitaciones where tipo = 'Lujo';
select id from hoteles where NOMBRE = 'Hotel mini super More';
select usrBanco from usuarios where usr ='more'

insert into reservas (idHotel, idHabitacion, datein, dateout, cantidad)values (1, 1, '2017-05-05', '2017-05-07', 1)


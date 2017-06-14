select * from reservas;
delete from reservas where cantidad =3


EXEC requestHabitacion '1998-12-30 15:15', '1998-12-31 15:15', 'Hotel Super More', 'Lujo',3, 'more',''

create procedure requestHabitacion
@datein date,
@dateout date,
@hotelNombre varchar(30),
@tipoNombre varchar(30),
@cantidad int,
@usuario varchar(50),
@Respuesta varchar(20) out
as
DECLARE @diferiencia int
declare @idHotel int
declare @idHabitacion int
declare @precio int
declare @userBanco varchar(50)


select @diferiencia = count(*)from reservas where (reservas.datein between @datein and @dateout) or reservas.dateout between @datein and @dateout
--select @diferiencia = DATEDIFF(dd, @datein, @dateout)

if(@diferiencia < 1)
	begin
		select @idHotel = hoteles.id from hoteles where hoteles.nombre = @hotelNombre;
		select @idHabitacion = habitaciones.id from habitaciones where habitaciones.tipo = @tipoNombre;
		select @precio = habitaciones.precio from habitaciones  where habitaciones.tipo = @tipoNombre;

		insert into reservas (idHotel, idHabitacion, datein, dateout, cantidad)
		values (@idHotel, @idHabitacion, @datein, @dateout, @cantidad);

		select @userBanco = usuarios.usrBanco from usuarios where usuarios.usr = @usuario;
		select @Respuesta = @cantidad * @precio

		print @Respuesta 
	end
go




select count(*) from reservas where (reservas.datein between '2017-05-05' and '2017-05-06') or reservas.dateout between '2017-05-05' and '2017-05-06'





select * from reservas;
update reservas set cinfirmacion = 1 where cinfirmacion = 0

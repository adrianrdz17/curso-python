import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='gustavo01',
    database='prueba'
)

cursor = mydb.cursor()

# listar datos
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

# listar datos con limite
cursor.execute('select * from Usuario limit 1')
resultado = cursor.fetchall()
print(resultado)

# ver definiciones de tabla
# cursor.execute('show create table Usuario')

# insertar datos
# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario', 45)

# actualizar datos
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo@micorreo.com', 4)
# cursor.execute(sql, values)

# Confirmando cambios en la base de datos sql
# mydb.commit()
# print(cursor.rowcount)

# eliminar datos
# sql = 'delete from Usuario where id = %s'
# values = (4, )
# cursor.execute(sql, values)
# mydb.commit()

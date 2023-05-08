from backend.models.mysql_connection_pool import MySQLPool
import requests
import mysql.connector
class AlumnoModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_alumno(self, dni_alumno):    
        params = {'dni_alumno' : dni_alumno}      
        rv = self.mysql_pool.execute("""SELECT * from alumnos where dni_alumno = %(dni_alumno)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni_alumno': result[0],'id_usuario': result[1], 'nombre': result[2], 'apellido': result[3], 'fecha_nacimiento':result[4], 'foto':result[5], 'vector':result[6]}
            data.append(content)
            content = {}
        return data

    def get_alumnos(self):  
        rv = self.mysql_pool.execute("""SELECT * from alumnos""")  
        data = []
        content = {}
        for result in rv:
            content = {'dni_alumno': result[0],'id_usuario': result[1], 'nombre': result[2], 'apellido': result[3], 'fecha_nacimiento':result[4], 'foto':result[5], 'vector':result[6]}
            data.append(content)
            content = {}
        return data

    def create_alumno(self, dni_alumno, id_usuario, nombre, apellido, fecha_nacimiento, foto):

        response = requests.post(" http://127.0.0.1:9000/openfaceAPI", files = {"file" : open("{}".format(foto), "rb")})
        vector = response.json()

        data = {
            'dni_alumno' : dni_alumno,
            'id_usuario' : id_usuario,
            'nombre' : nombre,
            'apellido' : apellido,
            'fecha_nacimiento' : fecha_nacimiento,
            'foto' : foto,
            'vector' : vector["result"]
        }       
  
        query = """insert into alumnos (dni_alumno, id_usuario, nombre, apellido, fecha_nacimiento, foto, vector) 
            values (%(dni_alumno)s, %(id_usuario)s, %(nombre)s, %(apellido)s, %(fecha_nacimiento)s, %(foto)s, %(vector)s)"""

        try:
            cursor = self.mysql_pool.execute(query, data, commit=True)
        except mysql.connector.errors.IntegrityError as e:
            if e.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                return {'error' : "Error, el dni ya está registrado"}
            else:
                return {'Error' :"Error en la base de datos"}
        else:
            data['dni_alumno'] = cursor.lastrowid
            return data

    def update_alumno(self, dni_alumno, nombre, apellido, fecha_nacimiento, foto):   

        response = requests.post(" http://127.0.0.1:9000/openfaceAPI", files = {"file" : open("{}".format(foto), "rb")})
        vector = response.json()

        data = {
            'dni_alumno' : dni_alumno,
            'nombre' : nombre,
            'apellido' : apellido,
            'fecha_nacimiento' : fecha_nacimiento,
            'foto' : foto,
            'vector' : vector["result"]

        }  
        query = """update alumnos set nombre = %(nombre)s, apellido = %(apellido)s,
                    fecha_nacimiento= %(fecha_nacimiento)s, foto = %(foto)s, vector = %(vector)s where dni_alumno = %(dni_alumno)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_alumno(self, dni_alumno):    
        params = {'dni_alumno' : dni_alumno}      
        query = """delete from alumnos where dni_alumno = %(dni_alumno)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


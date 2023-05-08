from backend.models.mysql_connection_pool import MySQLPool
from backend.models.mysql_alumno_model import AlumnoModel
import requests
import numpy as np
import json

class AsistenciaModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_asistencia(self, id_asistencia):    
        params = {'id_asistencia' : id_asistencia}      
        rv = self.mysql_pool.execute("""SELECT * from asistencias where id_asistencia = %(id_asistencia)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_asistencia': result[0], 'dni_alumno': result[1], 'id_curso': result[2], 'fecha': result[3], 'hora_asistencia': result[4], 'tema_realizado': result[5], 'asistio': result[6]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.mysql_pool.execute("""SELECT * from asistencias""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_asistencia': result[0], 'dni_alumno': result[1], 'id_curso': result[2], 'fecha': result[3], 'hora_asistencia': result[4], 'tema_realizado': result[5], 'asistio': result[6]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, dni_alumno, id_curso, fecha, hora_asistencia, tema_realizado, foto):    
       
        response = requests.post(" http://127.0.0.1:9000/openfaceAPI", files = {"file" : open("{}".format(foto), "rb")})
        vector1 = np.array(response.json()["result"].strip('[]').split(), dtype=np.float)

        model = AlumnoModel()
        alumno = model.get_alumno(dni_alumno)
        vector2 = np.array(alumno[0]['vector'].strip('[]').split(), dtype=np.float)
           
        dist = np.linalg.norm(vector1-vector2)
        
        a = True if dist < 0.6 else False

        data = {
            'dni_alumno' : dni_alumno,
            'id_curso' : id_curso,
            'fecha' : fecha,
            'hora_asistencia' : hora_asistencia,
            'tema_realizado' : tema_realizado,
            'asistio' : a
        }
        

        query = """insert into asistencias (dni_alumno, id_curso, fecha, hora_asistencia, tema_realizado, asistio) 
            values (%(dni_alumno)s, %(id_curso)s, %(fecha)s, %(hora_asistencia)s, %(tema_realizado)s, %(asistio)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_asistencia'] = cursor.lastrowid
        return data

    def update_asistencia(self, id_asistencia, dni_alumno, id_curso, fecha, hora_asistencia, tema_realizado, asistio):    
        data = {
            'id_asistencia' : id_asistencia,
            'dni_alumno' : dni_alumno,
            'id_curso' : id_curso,
            'fecha' : fecha,
            'hora_asistencia' : hora_asistencia,
            'tema_realizado' : tema_realizado,
            'asistio' : asistio
        }  
        query = """update asistencias set dni_alumno = %(dni_alumno)s, id_curso = %(id_curso)s, fecha = %(fecha)s, hora_asistencia = %(hora_asistencia)s, tema_realizado = %(tema_realizado)s, asistio = %(asistio)s where id_asistencia = %(id_asistencia)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asistencia(self, id_asistencia): 
        params = {'id_asistencia' : id_asistencia}      
        query = """delete from asistencias where id_asistencia = %(id_asistencia)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


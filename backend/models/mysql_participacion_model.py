from backend.models.mysql_connection_pool import MySQLPool

class ParticipacionModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_participacion(self, id_participacion):    
        params = {'id_participacion' : id_participacion}      
        rv = self.mysql_pool.execute("SELECT * from participaciones where id_participacion=%(id_participacion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_participacion': result[0], 'dni_alumno': result[1], 'id_curso': result[2], 'total_puntos': result[3]}
            data.append(content)
            content = {}
        return data

    def get_participaciones(self):  
        rv = self.mysql_pool.execute("SELECT * from participaciones")  
        data = []
        content = {}
        for result in rv:
            content = {'id_participacion': result[0], 'dni_alumno': result[1], 'id_curso': result[2], 'total_puntos': result[3]}
            data.append(content)
            content = {}
        return data

    def create_participacion(self, dni_alumno, id_curso, total_puntos):    
        data = {
            'dni_alumno': dni_alumno,
            'id_curso': id_curso,
            'total_puntos': total_puntos
        }  
        query = """insert into participaciones (dni_alumno, id_curso, total_puntos) 
            values (%(dni_alumno)s, %(id_curso)s, %(total_puntos)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_participacion'] = cursor.lastrowid
        return data

    def update_participacion(self, id_participacion, dni_alumno, id_curso, total_puntos):    
        data = {
            'id_participacion': id_participacion,
            'dni_alumno': dni_alumno,
            'id_curso': id_curso,
            'total_puntos': total_puntos
        }  
        query = """update participaciones set dni_alumno = %(dni_alumno)s, id_curso = %(id_curso)s,
                    total_puntos= %(total_puntos)s where id_participacion = %(id_participacion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_participacion(self, id_participacion):    
        params = {'id_participacion' : id_participacion}      
        query = """delete from participaciones where id_participacion = %(id_participacion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result

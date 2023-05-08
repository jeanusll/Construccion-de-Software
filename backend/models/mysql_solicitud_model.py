from backend.models.mysql_connection_pool import MySQLPool

class SolicitudModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()
        
    def get_solicitud(self, id_solicitud):    
        params = {'id_solicitud' : id_solicitud}      
        rv = self.mysql_pool.execute("SELECT * from solicitudes where id_solicitud=%(id_solicitud)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_solicitud': result[0], 'id_asistencia': result[1], 'documento': result[2], 'justificacion': result[3]}
            data.append(content)
            content = {}
        return data

    def get_solicitudes(self):  
        rv = self.mysql_pool.execute("SELECT * from solicitudes")  
        data = []
        content = {}
        for result in rv:
            content = {'id_solicitud': result[0], 'id_asistencia': result[1], 'documento': result[2], 'justificacion': result[3]}
            data.append(content)
            content = {}
        return data

    def create_solicitud(self, id_asistencia, documento, justificacion):    
        data = {
            'id_asistencia': id_asistencia,
            'documento': documento,
            'justificacion': justificacion,
        }  
        query = """insert into solicitudes (id_asistencia, documento, justificacion) 
            values (%(id_asistencia)s, %(documento)s, %(justificacion)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_solicitud'] = cursor.lastrowid
        return data

    def update_solicitud(self, id_solicitud, id_asistencia, documento, justificacion):    
        data = {
            'id_solicitud': id_solicitud,
            'id_asistencia': id_asistencia,
            'documento': documento,
            'justificacion': justificacion,
        }  
        query = """update solicitudes set id_asistencia = %(id_asistencia)s, documento = %(documento)s,
                    justificacion= %(justificacion)s where id_solicitud = %(id_solicitud)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result': 1} 
        return result

    def delete_solicitud(self, id_solicitud):    
        params = {'id_solicitud': id_solicitud}      
        query = """delete from solicitudes where id_solicitud = %(id_solicitud)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result

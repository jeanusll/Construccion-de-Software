from backend.models.mysql_connection_pool import MySQLPool

class SeccionModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        rv = self.mysql_pool.execute("SELECT * from secciones where id_seccion=%(id_seccion)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'id_curso': result[2]}
            data.append(content)
            content = {}
        return data

    def get_secciones(self):  
        rv = self.mysql_pool.execute("SELECT * from secciones")  
        data = []
        content = {}
        for result in rv:
            content = {'id_seccion': result[0], 'nombre_seccion': result[1], 'id_curso': result[2]}
            data.append(content)
            content = {}
        return data

    def create_seccion(self, nombre_seccion, id_curso):    
        data = {
            'nombre_seccion' : nombre_seccion,
            'id_curso' : id_curso
        }  
        query = """insert into secciones (nombre_seccion, id_curso) 
            values (%(nombre_seccion)s, %(id_curso)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_seccion'] = cursor.lastrowid
        return data

    def update_seccion(self, id_seccion, nombre_seccion, id_curso):    
        data = {
            'id_seccion' : id_seccion,
            'nombre_seccion' : nombre_seccion,
            'id_curso' : id_curso

        }  
        query = """update secciones set nombre_seccion = %(nombre_seccion)s, id_curso=%(id_curso)s  where id_seccion = %(id_seccion)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_seccion(self, id_seccion):    
        params = {'id_seccion' : id_seccion}      
        query = """delete from secciones where id_seccion = %(id_seccion)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



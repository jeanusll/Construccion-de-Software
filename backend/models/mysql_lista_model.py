from backend.models.mysql_connection_pool import MySQLPool

class ListaModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_lista(self, id_lista):    
        params = {'id_lista' : id_lista}      
        rv = self.mysql_pool.execute("SELECT * from listas where id_lista=%(id_lista)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_lista': result[0], 'id_curso': result[1], 'dni_alumno': result[2], 'estado': result[3]}
            data.append(content)
            content = {}
        return data

    def get_listas(self):  
        rv = self.mysql_pool.execute("SELECT * from listas")  
        data = []
        content = {}
        for result in rv:
            content = {'id_lista': result[0], 'id_curso': result[1], 'dni_alumno': result[2], 'estado': result[3]}
            data.append(content)
            content = {}
        return data

    def create_lista(self, id_curso, dni_alumno, estado):    
        data = {
            'id_curso' : id_curso,
            'dni_alumno': dni_alumno,
            'estado': estado,
        }  
        query = """insert into listas (id_curso, dni_alumno, estado) 
            values (%(id_curso)s, %(dni_alumno)s, %(estado)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_lista'] = cursor.lastrowid
        return data

    def update_lista(self, id_lista, id_curso, dni_alumno, estado):    
        data = {
            'id_lista' : id_lista,
            'id_curso' : id_curso,
            'dni_alumno': dni_alumno,
            'estado': estado,
        }  
        query = """update listas set id_curso = %(id_curso)s, dni_alumno = %(dni_alumno)s,
                    estado= %(estado)s where id_lista = %(id_lista)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_lista(self, id_lista):    
        params = {'id_lista' : id_lista}      
        query = """delete from listas where id_lista = %(id_lista)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

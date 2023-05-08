from backend.models.mysql_connection_pool import MySQLPool

class AdministradorModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_administrador(self, id_administrador):    
        params = {'id_administrador' : id_administrador}      
        rv = self.mysql_pool.execute("""SELECT * from administradores where id_administrador = %(id_administrador)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_administrador': result[0], 'id_usuario': result[1]}
            data.append(content)
            content = {}
        return data

    def get_administradores(self):  
        rv = self.mysql_pool.execute("""SELECT * from administradores""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_administrador': result[0], 'id_usuario': result[1]}
            data.append(content)
            content = {}
        return data

    def create_administrador(self, id_usuario):    
        data = {
            'id_usuario' : id_usuario
        }  
        query = """insert into administradores (id_usuario) 
            values (%(id_usuario)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_administrador'] = cursor.lastrowid
        return data

    def update_administrador(self, id_administrador, id_usuario):    
        data = {
            'id_administrador' : id_administrador,  
            'id_usuario' : id_usuario   
        }  
        query = """update administradores set id_usuario = %(id_usuario)s where id_administrador = %(id_administrador)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_administrador(self, id_administrador):    
        params = {'id_administrador' : id_administrador}      
        query = """delete from administradores where id_administrador = %(id_administrador)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def profe_curso(self, profesor_dni, id_curso):     
        params = {
            'profesor_dni' : profesor_dni,
            'id_curso' : id_curso
        }      
        query = """insert into profesor_curso (profesor_dni, id_curso) values(%(profesor_dni)s, %(id_curso)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data
    


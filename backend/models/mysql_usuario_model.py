from backend.models.mysql_connection_pool import MySQLPool

class UsuarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        rv = self.mysql_pool.execute("""SELECT * from usuarios where id_usuario = %(id_usuario)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'id_grupo_usuario': result[1], 'email': result[2],'contraseña': result[3]}
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):  
        rv = self.mysql_pool.execute("""SELECT * from usuarios""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'id_grupo_usuario': result[1], 'email': result[2],'contraseña': result[3]}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, id_grupo_usuario, email, contra):    
        data = {
            'id_grupo_usuario' : id_grupo_usuario,
            'email' : email,
            'contra' : contra
        }  
        query = """insert into usuarios (id_grupo_usuario, email, contra) 
            values (%(id_grupo_usuario)s, %(email)s, %(contra)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_usuario'] = cursor.lastrowid
        return data

    def update_usuario(self, id_grupo_usuario, id_usuario, contra, email):    
        data = {
            'id_usuario' : id_usuario,  
            'id_grupo_usuario' : id_grupo_usuario,
            'contra' : contra,            
            'email' : email            
        }  
        query = """update usuarios set id_grupo_usuario = %(id_grupo_usuario)s, contra = %(contra)s, email = %(email)s where id_usuario = %(id_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuarios where id_usuario = %(id_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


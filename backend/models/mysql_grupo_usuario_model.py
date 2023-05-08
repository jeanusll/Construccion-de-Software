from backend.models.mysql_connection_pool import MySQLPool

class GrupoUsuarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_grupo_usuario(self, id_grupo_usuario):    
        params = {'id_grupo_usuario' : id_grupo_usuario}      
        rv = self.mysql_pool.execute("""SELECT * from grupo_usuarios where id_grupo_usuario = %(id_grupo_usuario)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo_usuario': result[0], 'accesos': result[1],'restricciones': result[2]}
            data.append(content)
            content = {}
        return data

    def get_grupo_usuarios(self):  
        rv = self.mysql_pool.execute("""SELECT * from grupo_usuarios""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_grupo_usuario': result[0], 'accesos': result[1],'restricciones': result[2]}
            data.append(content)
            content = {}
        return data

    def create_grupo_usuario(self, accesos, restricciones):    
        data = {
            'accesos' : accesos,
            'restricciones' : restricciones
        }  
        query = """insert into grupo_usuarios (accesos, restricciones) 
            values (%(accesos)s, %(restricciones)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_grupo_usuario'] = cursor.lastrowid
        return data

    def update_grupo_usuario(self, id_grupo_usuario, accesos, restricciones):    
        data = {
            'id_grupo_usuario' : id_grupo_usuario,            
            'accesos' : accesos,            
            'restricciones' : restricciones            
        }  
        query = """update grupo_usuarios set accesos = %(accesos)s, restricciones = %(restricciones)s where id_grupo_usuario = %(id_grupo_usuario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_grupo_usuario(self, id_grupo_usuario):    
        params = {'id_grupo_usuario' : id_grupo_usuario}      
        query = """delete from grupo_usuarios where id_grupo_usuario = %(id_grupo_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


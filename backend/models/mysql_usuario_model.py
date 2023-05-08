from backend.models.mysql_connection_pool import MySQLPool
import bcrypt

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
            content = {'id_usuario': result[0], 'id_grupo_usuario': result[1], 'email': result[2],'contraseña': str(result[3])}
            data.append(content)
            content = {}
        return data

    def create_usuario(self, id_grupo_usuario, email, contra):   
        contra_encrip = self.encriptar_password(contra)
        data = {
            'id_grupo_usuario' : id_grupo_usuario,
            'email' : email,
            'contra' : contra_encrip
        }       
        

        query = """insert into usuarios (id_grupo_usuario, email, contra) 
            values (%(id_grupo_usuario)s, %(email)s, %(contra)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   
        data['id_usuario'] = cursor.lastrowid
        data['contra'] = contra_encrip.decode('utf-8')

        return data

    def update_usuario(self, id_usuario, id_grupo_usuario, email, contra_anterior, contra_nueva):    
        data = {
            'id_usuario' : id_usuario,  
            'id_grupo_usuario' : id_grupo_usuario,
            'contra' : self.encriptar_password(contra_nueva),            
            'email' : email,
        }  

        usuario = self.get_usuario(id_usuario)
        print(usuario[0]["contraseña"].encode('utf-8'))
        print(contra_anterior)
        if self.verificar_password(contra_anterior, usuario[0]["contraseña"].encode('utf-8')):

            query = """update usuarios set id_grupo_usuario = %(id_grupo_usuario)s, contra = %(contra)s, email = %(email)s where id_usuario = %(id_usuario)s"""    
            cursor = self.mysql_pool.execute(query, data, commit=True)   

            result = {'result':1} 
            return result
        else:
            return {"Error": "Contraseña anterior no coincide"}

    def delete_usuario(self, id_usuario):    
        params = {'id_usuario' : id_usuario}      
        query = """delete from usuarios where id_usuario = %(id_usuario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

    def iniciar_sesion(self, email, contra):    
        params = {
            'email' : email,
            'contra' : contra
        }      
        query = """select * from usuarios where email = %(email)s"""    
        
        rv = self.mysql_pool.execute(query, params, commit=True)
        data = []
        content = {}
        for result in rv:
            content = {'id_usuario': result[0], 'id_grupo_usuario': result[1], 'email': result[2],'contraseña': result[3]}
            data.append(content)
            content = {}

        if len(data) > 0:

            if self.verificar_password(contra, data[0]["contraseña"]):
                return data
            else:
                return {"Error": "Contraseña incorrecta"}
        else:
            return {"Error" : "No se pudo encontrar email"}


    def encriptar_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    def verificar_password(self, password, hashed):
        return bcrypt.checkpw(password.encode('utf-8'), hashed)

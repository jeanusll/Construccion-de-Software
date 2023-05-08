from backend.models.mysql_connection_pool import MySQLPool

class ProfesorModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_profesor(self, profesor_dni):    
        params = {'profesor_dni' : profesor_dni}      
        rv = self.mysql_pool.execute("SELECT * from profesores where profesor_dni=%(profesor_dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'profesor_dni': result[0], 'profesor_nombre': result[1], 'profesor_apellido': result[2], 'profesor_fecha_nac': result[3], 'id_usuario': result[4]}
            data.append(content)
            content = {}
        return data

    def get_profesores(self):  
        rv = self.mysql_pool.execute("SELECT * from profesores")  
        data = []
        content = {}
        for result in rv:
            content = {'profesor_id': result[0], 'profesor_nombre': result[1], 'profesor_apellido': result[2], 'profesor_fecha_nac': result[3], 'id_usuario': result[4]}
            data.append(content)
            content = {}
        return data

    def create_profesor(self, profesor_dni, profesor_nombre, profesor_apellido, profesor_fecha_nac, id_usuario):    
        data = {
            'profesor_dni' : profesor_dni,
            'profesor_nombre' : profesor_nombre,
            'profesor_apellido' : profesor_apellido,
            'profesor_fecha_nac': profesor_fecha_nac,
            'id_usuario' : id_usuario
        }  
        query = """insert into profesores (profesor_dni, profesor_nombre, profesor_apellido, profesor_fecha_nac, id_usuario) 
            values (%(profesor_dni)s, %(profesor_nombre)s, %(profesor_apellido)s, %(profesor_fecha_nac)s, %(id_usuario)s)"""    
        
        try:
            cursor = self.mysql_pool.execute(query, data, commit=True)
        except mysql.connector.errors.IntegrityError as e:
            if e.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                return {'error' : "Error, el dni ya está registrado"}
            else:
                return {'Error' :"Error en la base de datos"}
        else:
            data['profesor_dni'] = cursor.lastrowid
            return data

    def update_profesor(self, profesor_dni, profesor_nombre, profesor_apellido, profesor_fecha_nac, id_usuario):    
        data = {
            'profesor_dni' : profesor_dni,
            'profesor_nombre' : profesor_nombre,
            'profesor_apellido' : profesor_apellido,
            'profesor_fecha_nac': profesor_fecha_nac,
            'id_usuario' : id_usuario
        }  
        query = """update profesores set profesor_nombre = %(profesor_nombre)s, profesor_apellido = %(profesor_apellido)s,
                    profesor_fecha_nac= %(profesor_fecha_nac)s, id_usuario=%(id_usuario)s where profesor_dni = %(profesor_dni)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_profesor(self, profesor_id):    
        params = {'profesor_dni' : profesor_dni}      
        query = """delete from profesores where profesor_dni = %(profesor_dni)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



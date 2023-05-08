from backend.models.mysql_connection_pool import MySQLPool

class CursoModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        rv = self.mysql_pool.execute("SELECT * from cursos where id_curso=%(id_curso)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1], 'semestre': result[2], 'horas_academicas': result[3], 'total_estudiantes': result[4]}
            data.append(content)
            content = {}
        return data

    def get_cursos(self):  
        rv = self.mysql_pool.execute("SELECT * from cursos")  
        data = []
        content = {}
        for result in rv:
            content = {'id_curso': result[0], 'nombre_curso': result[1], 'semestre': result[2], 'horas_academicas': result[3], 'total_estudiantes': result[4]}
            data.append(content)
            content = {}
        return data

    def create_curso(self, nombre_curso, semestre, horas_academicas):    
        data = {
            'nombre_curso' : nombre_curso,
            'semestre' : semestre,
            'horas_academicas': horas_academicas,
        }  
        query = """insert into cursos (nombre_curso, semestre, horas_academicas) 
            values (%(nombre_curso)s, %(semestre)s, %(horas_academicas)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_curso'] = cursor.lastrowid
        return data

    def update_curso(self, id_curso,nombre_curso, semestre, horas_academicas):    
        data = {
            'id_curso' : id_curso,
            'nombre_curso' : nombre_curso,
            'semestre' : semestre,
            'horas_academicas': horas_academicas,
        }  
        query = """update cursos set nombre_curso = %(nombre_curso)s, semestre = %(semestre)s,
                    horas_academicas= %(horas_academicas)s where id_curso = %(id_curso)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso(self, id_curso):    
        params = {'id_curso' : id_curso}      
        query = """delete from cursos where id_curso = %(id_curso)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 



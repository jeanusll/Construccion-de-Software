from backend.models.mysql_connection_pool import MySQLPool

class HorarioModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        rv = self.mysql_pool.execute("""SELECT * from horarios where id_horario = %(id_horario)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'id_curso': result[1],'hora_inicio': result[2],'hora_final': result[3],'dia': result[4],'aula': result[5]}
            data.append(content)
            content = {}
        return data

    def get_horarios(self):  
        rv = self.mysql_pool.execute("""SELECT * from horarios""")  
        data = []
        content = {}
        for result in rv:
            content = {'id_horario': result[0], 'id_curso': result[1],'hora_inicio': result[2],'hora_final': result[3],'dia': result[4],'aula': result[5]}
            data.append(content)
            content = {}
        return data

    def create_horario(self, id_curso, hora_inicio, hora_final, dia, aula):    
        data = {
            'id_curso' : id_curso,
            'hora_inicio' : hora_inicio,
            'hora_final' : hora_final,
            'dia' : dia,
            'aula' : aula
        }  
        query = """insert into horarios (id_curso, hora_inicio, hora_final, dia, aula) 
            values (%(id_curso)s, %(hora_inicio)s, %(hora_final)s, %(dia)s, %(aula)s)"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        data['id_horario'] = cursor.lastrowid
        return data

    def update_horario(self, id_horario, id_curso, hora_inicio, hora_final, dia, aula):    
        data = {
            'id_horario' : id_horario,
            'id_curso' : id_curso,
            'hora_inicio' : hora_inicio,
            'hora_final' : hora_final,
            'dia' : dia,
            'aula' : aula
        }  
        query = """update horarios set id_curso = %(id_curso)s, hora_inicio = %(hora_inicio)s, hora_final = %(hora_final)s, dia = %(dia)s, aula = %(aula)s where id_horario = %(id_horario)s"""    
        cursor = self.mysql_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_horario(self, id_horario):    
        params = {'id_horario' : id_horario}      
        query = """delete from horarios where id_horario = %(id_horario)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data


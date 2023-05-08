from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.alumno_blueprint import alumno_blueprint
from backend.blueprints.curso_blueprint import curso_blueprint
from backend.blueprints.usuario_blueprint import usuario_blueprint
from backend.blueprints.profesor_blueprint import profesor_blueprint
from backend.blueprints.seccion_blueprint import seccion_blueprint
from backend.blueprints.lista_blueprint import lista_blueprint
from backend.blueprints.participacion_blueprint import participacion_blueprint
from backend.blueprints.solicitud_blueprint import solicitud_blueprint
from backend.blueprints.seccion_blueprint import seccion_blueprint
from backend.blueprints.horario_blueprint import horario_blueprint
from backend.blueprints.grupo_usuario_blueprint import grupo_usuario_blueprint
from backend.blueprints.administrador_blueprint import administrador_blueprint
from backend.blueprints.asistencia_blueprint import asistencia_blueprint

app = Flask(__name__)

app.register_blueprint(alumno_blueprint)
app.register_blueprint(curso_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(profesor_blueprint)
app.register_blueprint(seccion_blueprint)
app.register_blueprint(lista_blueprint)
app.register_blueprint(participacion_blueprint)
app.register_blueprint(solicitud_blueprint)
app.register_blueprint(horario_blueprint)
app.register_blueprint(grupo_usuario_blueprint)
app.register_blueprint(administrador_blueprint)
app.register_blueprint(asistencia_blueprint)



cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
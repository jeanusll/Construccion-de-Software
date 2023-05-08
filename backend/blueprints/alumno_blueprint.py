from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_alumno_model import AlumnoModel
model = AlumnoModel()

alumno_blueprint = Blueprint('alumno_blueprint', __name__)

@alumno_blueprint.route('/alumno', methods=['PUT'])
@cross_origin()
def create_alumno():
    try:
        content = model.create_alumno(request.json['dni_alumno'], request.json['id_usuario'], request.json['nombre'], request.json['apellido'], request.json['fecha_nacimiento'], request.json['foto'])    
        return jsonify(content)
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 


@alumno_blueprint.route('/alumno', methods=['PATCH'])
@cross_origin()
def update_alumno():  

    try:
        content = model.update_alumno(request.json['dni_alumno'], request.json['id_usuario'], request.json['nombre'], request.json['apellido'], request.json['fecha_nacimiento'], request.json['foto'])
        return jsonify(content)    
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@alumno_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def delete_alumno():
    try:
        return jsonify(model.delete_alumno(int(request.json['dni_alumno'])))
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@alumno_blueprint.route('/alumno', methods=['POST'])
@cross_origin()
def alumno():
    try:
        return jsonify(model.get_alumno(int(request.json['dni_alumno'])))  
    except KeyError as e:
        return jsonify({'Error': f'Falta el campo obligatorio: {str(e)}' }), 400
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 

@alumno_blueprint.route('/alumnos', methods=['POST'])
@cross_origin()
def alumnos():
    try:
        return jsonify(model.get_alumnos())    
    except Exception as e:
        return jsonify({'Error': str(e)}), 500 
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
    content = model.create_alumno(request.json['dni_alumno'], request.json['id_usuario'], request.json['nombre'], request.json['apellido'], request.json['fecha_nacimiento'], request.json['foto'])    
    return jsonify(content)

@alumno_blueprint.route('/alumno', methods=['PATCH'])
@cross_origin()
def update_alumno():
    content = model.update_alumno(request.json['dni_alumno'], request.json['id_usuario'], request.json['nombre'], request.json['apellido'], request.json['fecha_nacimiento'], request.json['foto'])
    return jsonify(content)

@alumno_blueprint.route('/alumno', methods=['DELETE'])
@cross_origin()
def delete_alumno():
    return jsonify(model.delete_alumno(int(request.json['dni_alumno'])))

@alumno_blueprint.route('/alumno', methods=['POST'])
@cross_origin()
def alumno():
    return jsonify(model.get_alumno(int(request.json['dni_alumno'])))

@alumno_blueprint.route('/alumnos', methods=['POST'])
@cross_origin()
def alumnos():
    return jsonify(model.get_alumnos())
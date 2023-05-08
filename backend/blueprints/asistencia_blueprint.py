from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_asistencia_model import AsistenciaModel
model = AsistenciaModel()


asistencia_blueprint = Blueprint('asistencia_blueprint', __name__)


@asistencia_blueprint.route('/asistencia', methods=['PUT'])
@cross_origin()
def create_asistencia():
    content = model.create_asistencia(request.json['dni_alumno'], request.json['id_curso'], request.json['fecha'], request.json['hora_asistencia'], request.json['tema_realizado'], request.json['foto']) 
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['PATCH'])
@cross_origin()
def update_asistencia():
    content = model.update_asistencia(request.json['id_asistencia'], request.json['dni_alumno'], request.json['id_curso'], request.json['fecha'], request.json['hora_asistencia'], request.json['tema_realizado'], request.json['asistio']) 
    return jsonify(content)

@asistencia_blueprint.route('/asistencia', methods=['DELETE'])
@cross_origin()
def delete_asistencia():
    return jsonify(model.delete_asistencia(int(request.json['id_asistencia'])))

@asistencia_blueprint.route('/asistencia', methods=['POST'])
@cross_origin()
def asistencia():
    return jsonify(model.get_asistencia(int(request.json['id_asistencia'])))

@asistencia_blueprint.route('/asistencias', methods=['POST'])
@cross_origin()
def asistencias():
    return jsonify(model.get_asistencias())
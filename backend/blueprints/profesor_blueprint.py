from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_profesores_model import ProfesorModel
model = ProfesorModel()


profesor_blueprint = Blueprint('profesor_blueprint', __name__)


@profesor_blueprint.route('/profesor', methods=['PUT'])
@cross_origin()
def create_profesor():
    content = model.create_profesor(request.json['profesor_dni'], request.json['profesor_nombre'], request.json['profesor_apellido'], request.json['profesor_fecha_nac'],request.json['id_usuario'],request.json['id_curso'] )    
    return jsonify(content)

@profesor_blueprint.route('/profesor', methods=['PATCH'])
@cross_origin()
def update_profesor():
    content = model.update_profesor(request.json['profesor_dni'], request.json['profesor_nombre'], request.json['profesor_apellido'], request.json['profesor_fecha_nac'],request.json['id_usuario'],request.json['id_curso'] )    
    return jsonify(content)

@profesor_blueprint.route('/profesor', methods=['DELETE'])
@cross_origin()
def delete_profesor():
    return jsonify(model.delete_profesor(int(request.json['profesor_dni'])))

@profesor_blueprint.route('/profesor', methods=['POST'])
@cross_origin()
def profesor():
    return jsonify(model.get_profesor(int(request.json['profesor_dni'])))

@profesor_blueprint.route('/profesores', methods=['POST'])
@cross_origin()
def profesores():
    return jsonify(model.get_profesores())
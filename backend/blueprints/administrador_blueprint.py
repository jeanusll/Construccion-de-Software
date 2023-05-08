from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_administrador_model import AdministradorModel
model = AdministradorModel()


administrador_blueprint = Blueprint('administrador_blueprint', __name__)


@administrador_blueprint.route('/administrador', methods=['PUT'])
@cross_origin()
def create_administrador():
    content = model.create_administrador(request.json['id_usuario'])    
    return jsonify(content)

@administrador_blueprint.route('/administrador', methods=['PATCH'])
@cross_origin()
def update_administrador():
    content = model.update_administrador(request.json['id_administrador'], request.json['id_usuario'])    
    return jsonify(content)

@administrador_blueprint.route('/administrador', methods=['DELETE'])
@cross_origin()
def delete_administrador():
    return jsonify(model.delete_administrador(int(request.json['id_administrador'])))

@administrador_blueprint.route('/administrador', methods=['POST'])
@cross_origin()
def administrador():
    return jsonify(model.get_administrador(int(request.json['id_administrador'])))

@administrador_blueprint.route('/administradores', methods=['POST'])
@cross_origin()
def administradores():
    return jsonify(model.get_administradores())